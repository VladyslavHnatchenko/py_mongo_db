import pymongo

"""Create a database called "test_db":"""
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["test_db"]

"""Create a collection called "clients":"""
my_col = my_db["clients"]
# print(my_client.list_database_names())

"""Find the first document in the customers collection:"""
x = my_col.find_one()
print(x)

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
