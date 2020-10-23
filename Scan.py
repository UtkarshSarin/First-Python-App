from pymongo import MongoClient
import pymongo
from cv2 import cv2
import json
from tkinter import *
import time
from tkinter.ttk import *



def video_reader():
    client = pymongo.MongoClient("mongodb+srv://python:python@cinema.u2fpu.mongodb.net/CinemaBackend?retryWrites=true&w=majority")
    db = client.CinemaAdmin
    mydb = client["CinemaAdmin"]
    mycol = mydb["Tickets"]
    cam = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            break
        cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("Q"):
            break
    # print(data)
    DA = json.loads(data)
    unique_id = db.Tickets.find_one(DA)
    unique_id_UPDATE = db.Tickets.find_one(DA,{'_id': False})
    if(unique_id_UPDATE['Ticket Status'] == "Used"):
        

        window = Tk()
        window.geometry("400x200")
        window['bg']='red'
        
        window.title("Welcome to Sarins Cinema")
        lbl = Label(window, text=f'Oops! Ticket Already Used!')

        lbl.grid(column=0, row=1)

        window.mainloop()
        time.sleep(5)



    else:
        db.Tickets.update_one(DA, {"$set":{"Ticket Status":"Used"}})
    
        window = Tk()
        window.geometry("400x200")
        window['bg']='green'
        
        window.title("Welcome to Sarins Cinema")
        lbl = Label(window, text=f'Welcome! Enjoy Your {unique_id_UPDATE["Movie"]}')

        lbl.grid(column=0, row=1)
        time.sleep(5)
        window.mainloop()
        time.sleep(5)
        window.destroy()




     


 
    exit(0)
    cam.release()
    cv2.destroyAllWindows()
    

    
    


    # col.update_one({"name":"John"}, {"$set":{"name":"Joseph"}})