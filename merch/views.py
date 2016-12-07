from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient

mongo = MongoClient()

# Create your views here.
def index(request):
    db = mongo['main']
    users = db['users']
    admin = users.find_one({'_id': 'admin'})
    ans = str(admin['name'])
    return HttpResponse("Hello, world. You're at the poll." + ans)
