from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password): #DEBUG (self, username, password) might need added, (self) originally 
        # Initializeg the MongoClient
        # Connection Variables
        #
        #USER = 'aacuser' #commented out to update with user password reqs 
        #PASS = 'password' #commented out to update with user password reqs
        HOST = 'nv-desktop-services.apporto.com'
        PORT = '30756'
        DB = 'AAC'
        COL = 'animals'
        # Create a connection string
        #connection_string = f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/" #commented out original, works
        connection_string = f"mongodb://{username}:{password}@{HOST}:{PORT}/"        
        #
        # Initialize Connection
        #
        self.client = MongoClient(connection_string)
        self.database = self.client[DB]
        self.collection = self.database[COL]
        

# Complete this create method to implement the C in CRUD. NOTE: looks complete to me!
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary
                return result.acknowledged #returns True if insertion successful
            except Exception as e:
                print(f"Error occurred: {e}")
                return False #Return false if exception occurred
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, query=None):
    #reads documents from 'animals' collection,   if no query is made, returns all documents
        try:
            if query is None:
                #no query? returns all documents
                result = list(self.database.animals.find())
            else:
                #have query? returns matching document
                result = list(self.database.animals.find(query))
            #if no documents are found
            if not result:
                print("No documents found")
                return None
        
            return result
        except Exception as e:
            raise Exception(f"Error reading documents: {e}")

# Create method to update the database, implement the U in CRUD
    def update(self, query, update_values):
        #updates document in the 'animals' collection from a query
        try:
            if not query or not update_values:
                raise ValueError("Both query and update values must be provided.")
            #use update_one 
            update_result = self.database.animals.update_one(query, {"$set": update_values})
        
            if update_result.matched_count == 0:
                print("No matching documents found.")
                return None
        
            return {
                "matched count": update_result.matched_count,
                "modified count": update_result.modified_count
            
            }
        except Exception as e:
            raise Exception(f"Error updating documents: {e}")
            
# Create method to delete from the database, implement the D in CRUDC
    def delete(self, query):
        #deletes query document in the 'animals' collection 
        try:
            if not query:
                raise ValueError("Query must be provided for deletion.")
            #delete the document, using 'delete_one'
            delete_result = self.database.animals.delete_one(query)
            
            if delete_result.deleted_count == 0:
                print("No matching documents found, nothing deleted.")
                return None
            
            return {"deleted_count": delete_result.deleted_count}
        except Exception as e:
            raise Exception(f"Error deleting documents: {e}")
        
            
        

