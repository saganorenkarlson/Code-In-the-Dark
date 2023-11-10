from celery import shared_task
import datetime
from django.views.decorators.csrf import csrf_exempt
import pymongo
from django.http import HttpResponseBadRequest, JsonResponse
from pymongo.errors import ServerSelectionTimeoutError
import certifi
import os
from firebase_admin import auth
from .firebase_config import firebase_app
import random
import re
from pymongo import MongoClient


mongo_username = os.getenv('DATABASE_USER')
mongo_password = os.getenv('DATABASE_PASS')
try:
    connection = f"mongodb+srv://{mongo_username}:{mongo_password}@codeinthedarkdb.t2johht.mongodb.net/test"
    mongo_client = pymongo.MongoClient(connection, tlsCAFile=certifi.where())
    db = mongo_client['codeinthedark']
    collection = db['game']
    print("Connected successfully!")
    
except ServerSelectionTimeoutError:
    print("Failed to connect to MongoDB server.")


@shared_task(bind=True)
@csrf_exempt
def generateRandomAndupdateHTML(request):

    # Get the new code from the request data
    new_code = " "
    
    cursor = collection.find({'_id': 'parent'})

    for document in cursor:
        parent= document['code']
        
    cursor = collection.find({'_id': 'elements'})
    for document in cursor:
        element=document['code']
        print()
            
    randomHowManyParentDiv =  random.randint(2, 5)
    
    for i in range(0,randomHowManyParentDiv):
        randomParentDiv =  random.randint(0, len(parent)-1)
        new_code += parent[randomParentDiv]
        
        randomHowManyInParentDiv = random.randint(1,4)
        for j in range(0,randomHowManyInParentDiv):
            randomElement = random.randint(0, len(element)-1)
            new_code+= element[randomElement]
        new_code+= "</div>"
        
    pattern=   r'\$'        
    patternn=  r'\&'
    
    new_code = re.sub(pattern, lambda m: generateRandomColor(), new_code)
    new_code = re.sub(patternn, lambda m: str(generateRandomNumber()), new_code)
        
    # Update the document with _id=1
    collection.update_one(
        {'_id': "1"},
        {'$set': {'code': new_code}}
    )  
    return str(new_code)

def generateRandomColor():
    colors= ['red','orange','yellow','green','blue','purple','pink',
    'brown','gray','black','teal','maroon','navy','olive','silver','lime','aqua','fuchsia','indigo']
    randomnum= random.randint(0, 18)
    return colors[randomnum]
    
def generateRandomNumber():
    return random.randint(1, 15)*10
    