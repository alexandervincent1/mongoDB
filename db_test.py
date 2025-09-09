# import pymongo
# from pymongo import MongoClient
# # Anslut till din MongoDB Atlas-databas
# anslutningsstrang = "mongodb+srv://alexandervincent_db_user:UQ3vRAUst_pA6_b@cluster0.dozqe8u.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(anslutningsstrang)
# # Välj databas och samling (de skapas automatiskt om de inte finns)
# db = client['MinSkola']
# samling = db['elever']
# # ---- SKAPA DATA ----
# # Ett Python-dictionary som representerar en elev
# ny_elev = {
# "namn": "Anna Andersson",
# "program": "Teknik",
# "årskurs": 2,
# "kurser": ["Matematik", "Programmering 1"]
# }
# # Infoga dokumentet i samlingen
# samling.insert_one(ny_elev)
# print(f"Lade till eleven: {ny_elev['namn']}")
# # ---- HÄMTA DATA ----
# print("\nSöker efter Anna...")
# # Hitta ett dokument som matchar en fråga
# hittad_elev = samling.find_one({"namn": "Anna Andersson"})
# if hittad_elev:
#     print(f"Hittade eleven: {hittad_elev['namn']}, som går i årskurs {hittad_elev['årskurs']}")

# else:
#     print("Kunde inte hitta eleven.")
# # Stäng anslutningen
#     client.close()





import pymongo
from pymongo import MongoClient
anslutning ="mongodb+srv://alexandervincent_db_user:UQ3vRAUst_pA6_b@cluster0.dozqe8u.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(anslutning)
db = client['MittLager']
# ny_data = {
# "produkt": "Skrivbord",
# "pris": 1200,
# "lager": 15
# }
# db.collection.insert_one(ny_data)
# ny_data = {
# "produkt": "Stol",
# "pris": 300,
# "lager": 50

# }
# db.collection.insert_one(ny_data)


find = db.collection.find({"produkt": {"$in": ["Skrivbord", "Stol"]}})
if find:
    for item in find:
        print(f"Hittade produkten: {item['produkt']}, som kostar {item['pris']} kr och har {item['lager']} i lager")



namn = input("Skriv ditt namn\n")
epost = input("Skriv din epost\n")

ny_data = {
"namn": namn,
"epost": epost
}
find1 = db.users.find_one({"epost": epost})
if find1==None:
    db.users.insert_one(ny_data)
    print("Du är nu registrerad")
else:
    print("Du är redan registrerad")



client.close()