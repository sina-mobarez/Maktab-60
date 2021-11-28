import time
import json
import datetime

from pymongo import MongoClient
from pymongo import ASCENDING

from settings import MONGO_HOST, MONGO_USER, MONGO_PASS


class Database:

    def initialize(self):
        try:
            mongo_client = MongoClient('localhost', 27017)

            self.database = mongo_client['exam-database']

            self.book_collection = self.database['book']
            self.user_collection = self.database['user']

            # todo define collections here
            book = {"author": "",
                    "release-year": "",
                    "tags": [],
                    "likes": {"count": 0,
                              "user": []},
                    "comments": {
                        "count": 0,
                        "comment": [{"user": "", "text": ""}]
                    },
                    "date": datetime.datetime.utcnow()
                    }
            user = {
                "first-name": "",
                "last-name": "",
                "email": ""
            }
        except:
            print("Mongo Initialization Failed. Passing")


def __init__(self):
    self.initialize()
