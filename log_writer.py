import pymongo
import _datetime
from pymongo import MongoClient
anslutning ="mongodb+srv://alexandervincent_db_user:UQ3vRAUst_pA6_b@cluster0.dozqe8u.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(anslutning)
db = client['loggbok']
def log_writer(log_data):
    log_data ={"System Meddelande": "Systemet startades kl " + str(_datetime.datetime.now())}
    log_data["Användarmeddelande"] = input("Skriv loggmeddelande\n")
    db.logs.insert_one(log_data)

def log_reader():
    find = db.logs.find()
    if find:
        for item in find:
            print(f"{item['System Meddelande']}, {item['Användarmeddelande']}")

def log_deleter():
    db.logs.delete_many({})

# def log_sorter():
#     find = db.logs.find().sort("System Meddelande")

log_writer("Loggmeddelande")
log_reader()
# log_sorter()
if input("Vill du radera alla loggar? (ja/nej)\n").lower() == "ja":
    log_deleter()
    print("Alla loggar är raderade")
client.close()





            
