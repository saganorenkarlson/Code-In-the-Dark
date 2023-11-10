import datetime
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import pymongo
from pymongo.errors import ServerSelectionTimeoutError
import certifi
import os
from firebase_admin import auth
from .firebase_config import firebase_app
import random
import re
from pymongo import MongoClient

from app_backend.tasks import generateRandomAndupdateHTML

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


@csrf_exempt
def getHTML(request):
    if(request.method == 'GET'):     
       # Get all the documents from the collection
        cursor = collection.find({})
        results = []
        for document in cursor:
            results.append(document)
        
        data = {'results': results}
        return JsonResponse(data)


@csrf_exempt
def getHTMLToCompare(request):
    
       # Get all the documents from the collection
        cursor = collection.find({})
        results = []
        for document in cursor:
            results.append(document)
        
        return str(results[0])
    
