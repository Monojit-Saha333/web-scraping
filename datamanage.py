import pymongo

#collection_name='bars'
#records=[{'id':'1','name':'nokia'},{'id':'2','name':'realme'}]


def check_collection(collection_name):
    passwd='1lDoG5PbvMSRl9Hr'
    dbname='crawler_db'
    client=pymongo.MongoClient(f"mongodb+srv://monojit:{passwd}@cluster0.4m4cp.mongodb.net/{dbname}?retryWrites=true&w=majority")
    database=client['crawler_db']

    #print(database.list_collection_names())
    if collection_name in database.list_collection_names():
        return True
    else:
        return False

#check_collection(collection)

def create_collection_insert_records(collection_name,records):
    passwd = '1lDoG5PbvMSRl9Hr'
    dbname = 'crawler_db'
    client = pymongo.MongoClient(f"mongodb+srv://monojit:{passwd}@cluster0.4m4cp.mongodb.net/{dbname}?retryWrites=true&w=majority")
    database = client['crawler_db']
    collection=database[collection_name]
    inserted_records=collection.insert_many(records)
    #print('records inserted')

#create_collection_insert_records('phones',records)

def fetch_records(collection_name):
     passwd = '1lDoG5PbvMSRl9Hr'
     dbname = 'crawler_db'
     client = pymongo.MongoClient(f"mongodb+srv://monojit:{passwd}@cluster0.4m4cp.mongodb.net/{dbname}?retryWrites=true&w=majority")
     database = client['crawler_db']
     collection=database[collection_name]

     fetched_records=collection.find({})
     all_records=[]

     for indx,rows in enumerate(fetched_records):
         #print(f"{indx}:{rows}")
         all_records.append(rows)
     return all_records


#fetch_records('phones')



