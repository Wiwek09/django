from django.db import models
from db_connection import db

# Create your models here.

user_collection = db['next_career']
file_collection = db['file_upload']

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save(self):
        user_collection.insert_one({
             'first_name':self.first_name,
             'last_name':self.last_name,
             'email':self.email,
             'password':self.password
        })

    def find_by_email(email):
        user_collection.find_one({
            'email':email
        })

class 