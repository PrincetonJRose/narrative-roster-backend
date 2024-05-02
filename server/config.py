# Imports for config file
from flask import Flask, request, make_response, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
import os

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Set up:
    # generate a secrete key `python -c 'import os; print(os.urandom(16))'`
    # set the app.secret_key variable equal to what's printed in the console
    # app.secret_key = 'Secret Key here!'

    # or if you want it to be random every time you can set it like this
    # app.secret_key = os.urandom( 16 ).hex()

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate Bcrypt
bcrypt = Bcrypt( app )

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)
