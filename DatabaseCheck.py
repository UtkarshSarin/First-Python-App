from pymongo import MongoClient
import pymongo
client = pymongo.MongoClient("mongodb+srv://python:python@cinema.u2fpu.mongodb.net/CinemaBackend?retryWrites=true&w=majority")
    db = client.CinemaAdmin
    mydb = client["CinemaAdmin"]
    mycol = mydb["Tickets"]

    