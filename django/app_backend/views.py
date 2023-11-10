import datetime
from django.views.decorators.csrf import csrf_exempt
import pymongo
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from pymongo.errors import ServerSelectionTimeoutError
import certifi
import os
from firebase_admin import auth
from .firebase_config import firebase_app
from app_backend import views_game

from difflib import SequenceMatcher


mongo_username = os.getenv('DATABASE_USER')
mongo_password = os.getenv('DATABASE_PASS')

try:
    connection = f"mongodb+srv://{mongo_username}:{mongo_password}@codeinthedarkdb.t2johht.mongodb.net/test"
    mongo_client = pymongo.MongoClient(connection, tlsCAFile=certifi.where())
    db = mongo_client['codeinthedark']
    collection = db['users']
    print("Connected successfully!")
    
except ServerSelectionTimeoutError:
    print("Failed to connect to MongoDB server.")


def validate(username, authorization_header):
    if(authorization_header):
        _, token = authorization_header.split(' ')
    else:
        return False

    try:
        decoded_token = auth.verify_id_token(token,firebase_app)
        if decoded_token['email'] != username:
            raise auth.InvalidIdTokenError('Access token does not match username')
    except auth.InvalidIdTokenError:
            return False
    
    return True


def calculate_similarity(html1, html2):
    # Remove whitespace and newlines from the HTML snippets
    html1 = ''.join(html1.split())
    html2 = ''.join(html2.split())

    # Calculate the similarity ratio using SequenceMatcher
    similarity_ratio = SequenceMatcher(None, html1, html2).ratio()

    return  round(similarity_ratio, 2)

@csrf_exempt
def user(request):
    if(request.method == 'GET'):        
        username = request.GET.get('username', None)
        print(username)
        if(not validate(username,request.META.get('HTTP_AUTHORIZATION', ''))):
            return HttpResponseBadRequest('Invalid access')
        user = collection.find_one({'username': username})   
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        data = {'results': user['results']}
        return JsonResponse(data)   
    elif(request.method == 'POST'):
        username = request.GET.get('username', None)
        if(not validate(username,request.META.get('HTTP_AUTHORIZATION', ''))):
            return HttpResponseBadRequest('Invalid access')
        new_user = {
            "username" : username,
            "results": [],
            "friends": [],
            "requests_received": [],
            "requests_sent": []
        }
        collection.insert_one(new_user)

        return JsonResponse(username, safe=False)
    elif(request.method == 'PUT'):
        
        username = request.GET.get('username', None)
        existing_document = collection.find_one({'username': username})
        if(not validate(username,request.META.get('HTTP_AUTHORIZATION', ''))):
            return HttpResponseBadRequest('Invalid access')
        htmlresult = request.GET.get('result',0)
        htmlcorrect = views_game.getHTMLToCompare("GET")
        percentage= calculate_similarity(htmlresult, htmlcorrect)*100
        today = datetime.date.today().strftime("%Y-%m-%d")
        if(len(existing_document['results']) == 0 or (existing_document['results'][len(existing_document['results'])-1]  )!=today):
            collection.update_one({'username': username}, {'$push': {'results': {'date':today, 'percentage': percentage}}})
            updated_user = collection.find_one({'username': username})
            data = {'results': updated_user['results'], 'username': updated_user['username'], 'friends': updated_user['friends']}
            return JsonResponse(data,safe=False)
        else:
            return JsonResponse("alreadyDone",safe=False)

@csrf_exempt
def friends(request):
    if(request.method == 'GET'):
        username = request.GET.get('username', None)
        if(not validate(username,request.META.get('HTTP_AUTHORIZATION', ''))):
            return HttpResponseBadRequest('Invalid access')
        user = collection.find_one({'username': username})   
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        friends = user.get('friends',[])

        friends_usernames = [friend['username'] for friend in friends]
        friends_documents = collection.find({'username': {'$in': friends_usernames}})
        friends_info = []
        for friend in friends_documents:
            friend_info = {'username': friend['username'], 'results': friend['results']}
            friends_info.append(friend_info)

        data = {'friends': friends_info}
        return JsonResponse(data)   
    if(request.method == 'DELETE'):
        username = request.GET.get('username', None)
        target_username = request.GET.get('target_username', None)
        
        if not validate(username, request.META.get('HTTP_AUTHORIZATION', '')):
            return HttpResponseBadRequest('Invalid access')
        
        user = collection.find_one({'username': username})
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        friend = collection.find_one({'username': target_username})
        if not friend:
            return HttpResponseBadRequest('Friend not found')
        
        friends = user.get('friends', [])
        friends = [friend for friend in friends if friend['username'] != target_username]
        collection.update_one({'username': username}, {'$set': {'friends': friends}})
        
        friends = friend.get('friends', [])
        friends = [friend for friend in friends if friend['username'] != username]
        collection.update_one({'username': target_username}, {'$set': {'friends': friends}})
        
        user = collection.find_one({'username': username})
        friends = user.get('friends', [])
        friends_usernames = [friend['username'] for friend in friends]
        friends_documents = collection.find({'username': {'$in': friends_usernames}})
        friends_info = []
        for friend in friends_documents:
            friend_info = {'username': friend['username'], 'results': friend['results']}
            friends_info.append(friend_info)
        
        data = {'friends': friends_info}
        return JsonResponse(data)
    

@csrf_exempt
def top(request):
    if request.method == 'GET':
        today = datetime.date.today().strftime("%Y-%m-%d")
        top_results = collection.aggregate([
        {'$match': {'results.date': today}},
        {'$unwind': '$results'},
        {'$match': {'results.date': today}},
        {'$sort': {'results.percentage': -1}},
        {'$group': {'_id': '$username', 'percentage': {'$first': {'$toDouble': '$results.percentage'}}}},
        {'$sort': {'percentage': -1}},
        {'$limit': 5}
        ])

        result_list = [{'username': r['_id'], 'percentage': r['percentage']} for r in top_results]

        return JsonResponse({'results': result_list})
    
    
@csrf_exempt
def user_results(request):
    if request.method == 'GET':
        requesting_user = request.GET.get('requesting_user', None)
        target_user = request.GET.get('target_user', None)
        
        if not validate(requesting_user, request.META.get('HTTP_AUTHORIZATION', '')):
            return HttpResponseBadRequest('Invalid access')
        
        target_user_doc = collection.find_one({'username': target_user})
        if not target_user_doc:
            return HttpResponseBadRequest('Target user not found')
        
        current_month = datetime.date.today().strftime('%Y-%m')
        month_results = [result for result in target_user_doc['results'] if result['date'].startswith(current_month)]
        data = {'results': month_results}
        return JsonResponse(data)


@csrf_exempt
def friend_requests(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        
        if not validate(username, request.META.get('HTTP_AUTHORIZATION', '')):
            return HttpResponseBadRequest('Invalid access')
        
        user = collection.find_one({'username': username})   
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        requests_sent = user.get('requests_sent',[])
        requests_received = user.get('requests_received',[])

        data = {'requests_sent': requests_sent, 'requests_received': requests_received}
        return JsonResponse(data)
    elif request.method == 'POST':
        username = request.GET.get('requesting_user', None)
        target_user = request.GET.get('target_user', None)
        if not validate(username, request.META.get('HTTP_AUTHORIZATION', '')):
            return HttpResponseBadRequest('Invalid access')
        
        user = collection.find_one({'username': username})
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        target_user = collection.find_one({'username': target_user})
        if not target_user:
            return HttpResponseBadRequest('Target user not found')
        
        if username == target_user:
            return HttpResponseBadRequest('Invalid friend request')

        requests_sent = user.get('requests_sent', [])
        requests_sent.append({'username':target_user['username'] })
        collection.update_one({'username': username}, {'$set': {'requests_sent': requests_sent}})
        
        requests_received = target_user.get('requests_received', [])
        requests_received.append({'username': user['username']});
        collection.update_one({'username': target_user['username']}, {'$set': {'requests_received': requests_received}})
        
        data = {'requests_sent': requests_sent}
        return JsonResponse(data)
    elif request.method == 'PUT':
        answering_username = request.GET.get('answering_user', None)
        requesting_username = request.GET.get('requesting_user', None)
        answer = request.GET.get('answer',None).lower() == 'true'
        if not validate(answering_username, request.META.get('HTTP_AUTHORIZATION', '')):
            return HttpResponseBadRequest('Invalid access')
        answering_user = collection.find_one({'username': answering_username})
        if not answering_user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        requesting_user = collection.find_one({'username': requesting_username})
        if not requesting_user:
            return HttpResponseBadRequest('Requesting user not found')
        
        requests_sent = requesting_user.get('requests_sent', [])
        requests_sent = [request for request in requests_sent if request['username'] != answering_user['username']]
        collection.update_one({'username': requesting_username}, {'$set': {'requests_sent': requests_sent}})

        requests_received = answering_user.get('requests_received', [])
        requests_received = [request for request in requests_received if request['username'] != requesting_user['username']]
        collection.update_one({'username': answering_username}, {'$set': {'requests_received': requests_received}})
        
        #Accepting friend request
        if answer:
            friends = answering_user.get('friends', [])
            friends.append({'username': requesting_user['username']})
            collection.update_one({'username': answering_username}, {'$set': {'friends': friends}})

            friends = requesting_user.get('friends', [])
            friends.append({'username': answering_user['username']})
            collection.update_one({'username': requesting_username}, {'$set': {'friends': friends}})    

        friends = answering_user.get('friends', [])
        friends_usernames = [friend['username'] for friend in friends]
        friends_documents = collection.find({'username': {'$in': friends_usernames}})
        friends_info = []
        for friend in friends_documents:
            friend_info = {'username': friend['username'], 'results': friend['results']}
            friends_info.append(friend_info)
        
        data = {'friends': friends_info, 'requests_received': requests_received}
        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')


@csrf_exempt
def search_users(request):
    if ( request.method=='GET'):
        username = request.GET.get('username', None)
        if(not validate(username,request.META.get('HTTP_AUTHORIZATION', ''))):
            return HttpResponseBadRequest('Invalid access')
        user = collection.find_one({'username': username})   
        if not user:
            return HttpResponseBadRequest('Invalid access token or user not found')

        searchQuery = request.GET.get('searchQuery', None)
        if len(searchQuery)>0:
            # Search for usernames that include the given string
            query = {"username": {"$regex": searchQuery, "$ne": username}}
            results = collection.find(query)

            # Process the search results
            usernames = [user['username'] for user in results]
            return JsonResponse({'results':usernames})
        else:
            return JsonResponse({'results':[]})
