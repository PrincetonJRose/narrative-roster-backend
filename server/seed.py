#!/usr/bin/env python3

# Imports needed from other files
from random import randint, choice as rc
from faker import Faker
from app import app

fake = Faker()

# Don't forget to import models here too!!!
# from models import 

if __name__ == '__main__':
    with app.app_context():
        print("Seeding... 🌱")

        print( 'Wiping tables... 🧼' )
        # Clear all the tables!

        print( 'Database wiped! 🧹' )


        print( 'Creating ______ ...' )

        print( '_________ created!' )
