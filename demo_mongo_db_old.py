import pymongo

# -> Return the id Field <- #

# Create a database called "mydatabase":
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Create a collection called "customers":
mycol = mydb["customers"]

# Insert a record in the "customers" collection:
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)
# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# Return a list of your system's databases:
print(myclient.list_database_names())

# Check if the "customers" collection exists:
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

# Check if "mydatabase" exists:
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("We can't create db! \_^:^_/")
