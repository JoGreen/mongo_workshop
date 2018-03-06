from pymongo import MongoClient
import connection_data

class MongoInstance:


    def __init__(self, port=None, db_name=None):  #not usefuls using dbname here
        if port == None:
            self.port = connection_data.port
        else:
            self.port = port
        if db_name == None:
            self.db_name = connection_data.db_name
        else:
            self.db_name = db_name

        self.db = MongoClient(connection_data.url)[self.db_name]

    def getDbInstance(self): #deprecated
        return self.db





