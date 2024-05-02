#!/usr/bin/env python3

# Import everything we need for our api from our config file
from config import app, db, api, Resource, bcrypt, request, make_response, session
import requests, json

# Import models here!!!
# from models import 

# Routes!!!



if __name__ == '__main__':
    app.run( port=3000, debug=True )
