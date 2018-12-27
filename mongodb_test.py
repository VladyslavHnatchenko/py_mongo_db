import pymongo

"""Create a database called "test_db":"""
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["test_db"]

"""Create a collection called "clients":"""
my_col = my_db["clients"]
# print(my_client.list_database_names())

# for x in my_col.find():
#     print(x)

"""Limit the result to only return 5 documents:"""
my_result = my_col.find().limit(5)
for x in my_result:
    print(x)

"""Update all documents where the address starts with letter 'S':"""
# my_query = {"address": {"$regex": "^S"}}
# new_values = {"$set": {"name": "Minnie"}}
#
# x = my_col.update_many(my_query, new_values)
# print(x.matched_count, " documents updated.")

"""Change the address from 'Valley 345' to 'Canyon 123':"""
# my_query = {"address": "Valley 345"}
# new_values = {"$set": {"address": "Canyon 123"}}
#
# my_col.update_one(my_query, new_values)
#
# for x in my_col.find():
#     print(x)

"""Delete the 'customers' collection:"""
# my_col.drop()

"""Delete all documents in the 'clients' collection:"""
# x = my_col.delete_many({})
# print(x.deleted_count, " documents deleted.")

"""Delete all documents were the address starts with the letter S:"""
# my_query = {"address": {"$regex": "^S"}}
# x = my_col.delete_many(my_query)
#
# print(x.deleted_count, " documents deleted.")

"""Delete the document with the address 'Mountain 21':"""
# my_query = {"address": "Mountain 21"}
# my_col.delete_one(my_query)

"""Sort the result alphabetically bt name:"""
# my_doc = my_col.find().sort("address")

# Sort the result reverse alphabetically by name:
# my_doc = my_col.find().sort("name", -1)
#
# for x in my_doc:
#     print(x)

"""Find documents where the address starts with the letter 'S':"""
# my_query = {"address": {"$regex": "^S"}}
# my_doc = my_col.find(my_query)
#
# for x in my_doc:
#     print(x)

"""Find documents where the address starts with the letter 'S' or higher:"""
# my_query = {
#     "address": {"$gt": "S"}
# }
# my_doc = my_col.find(my_query)
# for x in my_doc:
#     print(x)


"""Find document(s) with the address "Park Lane 38":"""
# my_query = {"address": "Park Lane 38"}
# my_doc = my_col.find(my_query)
#
# for x in my_doc:
#     print(x)

"""Return only the names and addresses, not the _ids:"""
# for x in my_col.find({}, {"address": 0}):
#     print(x)

# for x in my_col.find({}, {"_id": 0, "name": 1, "address": 1}):
#     print(x)

"""Return all documents in the 'clients' collection, and print each document:"""
# for x in my_col.find():
#     print(x)

"""Find the first document in the customers collection:"""
# x = my_col.find_one()
# print(x)

"""Check if the "customers" collection exists:"""
# coll_list = my_db.list_collection_names()
# if "clients" in coll_list:
#     print("The collection exists.")
# else:
#     print("We can't create col! \_^:^_/")

"""Check if "test_db" exists:"""
# db_list = my_client.list_database_names()
# if "test_db" in db_list:
#     print("The database exists.")
# else:
#     print("We can't create db! \_^:^_/")

"""Insert a record in the "clients" collection:"""
# my_list = [
#     {"_id": 1, "name": "John", "address": "Highway 37"},
#     {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#     {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#     {"_id": 5, "name": "Michael", "address": "Valley 345"},
#     {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#     {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#     {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#     {"_id": 9, "name": "Susan", "address": "One way 98"},
#     {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#     {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#     {"_id": 12, "name": "William", "address": "Central st 954"},
#     {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#     {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = my_col.insert_many(my_list)
# print(x.inserted_ids)

"""Delete all documents in the "customers" collection:"""
# x = my_col.delete_many({})
# print(x.deleted_count, " documents deleted.")
