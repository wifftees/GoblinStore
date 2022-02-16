from pymongo import MongoClient

class StoreDB:
    @staticmethod
    def get_connection(username, password):
        return MongoClient(
            f"mongodb+srv://{username}:{password}@cluster0.z3tvv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        )  
        
    

        


