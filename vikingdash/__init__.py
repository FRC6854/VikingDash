"""
VikingDash - By FRC6854
Under the CC0 License
"""

__name__ = "VikingDash"
__authors__ = ["Owen Shaule"]
__license__ = "CC0"

from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "Secret!")
MONGODB_KEY = os.getenv("MONGODB_KEY", None)

print(f"""VikingDash Properties
Secret Key  : {SECRET_KEY}
MONGODB Key : {MONGODB_KEY}""")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

if MONGODB_KEY: mongodb_client = MongoClient(MONGODB_KEY)
else: mongodb_client = MongoClient()

database = mongodb_client["VikingDash"]
coopertitions = database.coopertitions
users = database.users

import vikingdash.methods

@app.context_processor
def context_processor():
    return dict(american_time=vikingdash.methods.american_time, alliance_list=vikingdash.methods.alliance_list)

import vikingdash.routes