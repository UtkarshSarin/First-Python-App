import qrcode
from PIL import Image
import json 
from twilio.rest import Client
import os
import string
import random
from pymongo import MongoClient
import pymongo
import qrcode
import cv2
import pyrebase
import rough
from tkinter import *
from tkinter.ttk import *




def BookMovie():


    window = Tk()

    window.title("Welcome to Sarins Cinema")
    MovieChoice = StringVar()
    MovieTiming = StringVar()
    NumberOfAdults = IntVar()
    NumberOfAdults.set(1)
    NumberOfKids = IntVar()
    NumberOfKids.set(1)
    MovieTiming.set("9:00 Am")
    NameOfUser = StringVar()

    combo = Combobox(window)

    combo['values']= ("The Shawshank Redemption", "In Pursuit of Happyness", "The Gods must be Crazy", "The Hacksaw Ridge","Kabir Singh","Select a Movie")

    combo.current(3) #set the selected item

    timing1 = Radiobutton(window,text='9:00 Am', value="9:00 Am", variable=MovieTiming)

    timing2 = Radiobutton(window,text='12:00 Pm', value="12:00 Pm", variable=MovieTiming)

    timing3 = Radiobutton(window,text='3:00 Pm', value="3:00 Pm", variable=MovieTiming)

    timing4 = Radiobutton(window,text='6:00 Pm', value="6:00 Pm", variable=MovieTiming)

    timing5 = Radiobutton(window,text='9:00 Pm', value="9:00 Pm", variable=MovieTiming)


    spin = Spinbox(window, from_=1, to=10, width=5, textvariable=NumberOfAdults)
    spinKids = Spinbox(window, from_=1, to=9, width=5, textvariable=NumberOfKids)


    lbl = Label(window, text="Select Movie Timings")

    lbl.grid(column=0, row=1)

    txt = Entry(window,width=10)

    lbl = Label(window, text="Name Of The User")

    lbl.grid(column=0, row=9)

    txt.grid(column=1, row=9)




    def clicked():

        print(txt.get(),combo.get(),MovieTiming.get(),NumberOfAdults.get())
        BookTicket(combo.get(),MovieTiming.get(),NumberOfAdults.get(),NumberOfKids.get())
        window.destroy()
    btn = Button(window, text="Book", command=clicked)

    combo.grid(column=0, row=0)

    timing1.grid(column=0, row=2)

    timing2.grid(column=0, row=3)

    timing3.grid(column=0, row=4)

    timing4.grid(column=0, row=5)

    timing5.grid(column=0, row=6)

    spin.grid(column=0,row=7)
    spinKids.grid(column=0,row=8)



    btn.grid(column=0, row=9)

    window.mainloop()



# this is not my code# this is not my code# this is not my code# this is not my code# this is not my code# this is not my code# this is not my code





def BookTicket(movie_input,timings_input,adults,kids):
    # //Module for generating Ticket ID
    # //Start 1
    N = 6

    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N)) 

    # print(str(res))
    # //End 1


    # //Module for Booking Details
    # //Start 2

    print(f"Ticket ID: {str(res)}")

    #  MOVIE
    # movie_input = input(f'Choose a movie from the following list: \n1: The Shawshank Redemption \n2: In Pursuit of Happyness \n3: The Gods must be Crazy \n4: The Hacksaw Ridge \n5: Kabir Singh \n')

    movie_json = '{"1":"The Shawshank Redemption","2":"In Pursuit of Happyness","3":"The Gods must be Crazy","4":"The Hacksaw Ridge","5":"Kabir Singh"}'

    movie_choice = json.loads(movie_json)

    # TIME
    # timings_input = input(f'Choose a movie timing from the following options : \n1: 9:00 am \n2: 12:00 pm \n3: 3:00 pm \n4: 6:00 pm \n5: 9:00 pm \n')

    timings_json = '{ "1":"9:00 am", "2": "12:00 pm", "3": "3:00 pm", "4": "6:00 pm", "5": "9:00 pm" }'

    timings_choice = json.loads(timings_json)

    # PEOPLE
    # adults = int(input("Enter the number of adults: "))
    # if adults >10:
    #     raise ValueError("Enter a Numeric Value less than upto 10")

    # kids = int(input("Enter the number of kids(Below the age of 15): "))
    # if kids >9:
    #     raise ValueError("Enter a Numeric Value less than upto 9")
    # # //PEOPLE

    # Billing
    total = adults * 150 + kids * 75

    tax = total * 0.18

    total_amt = int(total) + int(tax)

    print(f"The total bill amount is {total_amt}")
    # //Billing

    # //End 2

    # //Module for hosting QR Code
    # //Start
    
    # data = f"Your booking details are as follows \nUTN: {str(res)} \nMovie Name: {movie_choice[movie_input]} \nTime: {timings_choice[timings_input]} \nAdults: {adults} \nKids: {kids} \nTicket Total: ₹{int(total)} \nTax: ₹{int(tax)} \nTotal Amount: ₹{int(total_amt)} "
    # deets = f'{"UTN": {res}, "": {movie_choice[movie_input]}, "Time": {timings_choice[timings_input]}, "Adults": {adults}, "Kids": {kids}, "Ticket Total": {total}, "Tax": {tax}, "Total Amount": {total_amt}}'
    deets = {}
    deets["UTN"] = str(res)
    deets = json.dumps(deets)
    # print(deets)
    # output file name
    filename = "site.png"
    # generate qr code{'UTN': 'Y6EGAQ', 'Movie': 'The Shawshank Redemption', 'Time': '9:00 am'}
    img = qrcode.make(deets,version=1,    box_size=8,
)
    # save img to a file
    img.save(filename)


    img = cv2.imread("site.png")

    rough.pushcode()
    config = {
    "apiKey": "AIzaSyDCqXgsWsa6SAnAOWek_K4lDA0nV5yNC1Y",
    "authDomain": "SarinCinema.firebaseapp.com",
    "databaseURL": "https://sarincinema.firebaseio.com",
    "storageBucket": "sarincinema.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()
    

    link = storage.child("images").child("qrcode").get_url(1)
    # print(link)

    # //End


    # //Module for sending the Whatsapp Text
    # //Start 3
    account_sid = 'AC5238d3ca1f938161673c843ca85f8894'
    auth_token = '29bcf0f1b529fce3cae5520df428a5ad'
    client = Client(account_sid, auth_token)

    print(f"Your booking details are as follows \nUTN: {str(res)} \nMovie Name: {movie_input} \nTime: {timings_input} \nAdults: {adults} \nKids: {kids} \nTicket Total: {int(total)} \nTax: {int(tax)} \nTotal Amount: {int(total_amt)} \nThe Ticket is being sent to you via Whatsapp on your Registered Mobile Number")
    myticket = (f"*Welcome to Sarin's Cinema* \n\n\nYour booking details that will be sent to you are as follows \nUTN: {str(res)} \nMovie Name: {movie_input} \nTime: {timings_input} \nAdults: {adults} \nKids: {kids} \nTicket Total: {int(total)} \nTax: {int(tax)} \nTotal Amount: {int(total_amt)}")


    message = client.messages.create(
                                body=f"*Welcome to Sarin's Cinema* \n\n\nYour booking details are as follows: \nUTN: {str(res)} \nMovie Name: {movie_input} \nTime: {timings_input} \nAdults: {adults} \nKids: {kids} \nTicket Total: ₹{int(total)} \nTax: ₹{int(tax)} \nTotal Amount: ₹{int(total_amt)}",
                                media_url= f"{link}",
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+918384005257'
                            )

    print(message.sid)

    # //End 3

    # //Module for Sending data to the database
    # //Start 4
    client = pymongo.MongoClient("mongodb+srv://python:python@cinema.u2fpu.mongodb.net/CinemaBackend?retryWrites=true&w=majority")
    db = client.CinemaAdmin
    mydb = client["CinemaAdmin"]
    mycol = mydb["Tickets"]

    db.Tickets.insert_one(
        {"UTN": f"{str(res)}",
        "Ticket Status": "Not Used",
        "Movie": f"{movie_input}",
        "Timing": f"{timings_input}",
        "Adults": f"{adults}",
        "Kids": f"{kids}",  
        "Ticket Total": f"{total_amt}"})
    return None

    # //End 4


    # //Module for Generating QR Code
    # //Start5




    # detector = cv2.QRCodeDetector()

    # data, bbox, straight_qrcode = detector.detectAndDecode(img)

    # if bbox is not None:
    #     print(f"QRCode data:\n{data}")
    #     # display the image with lines
    #     # length of bounding box
    #     n_lines = len(bbox)
    #     for i in range(n_lines):
    #         # draw all lines
    #         point1 = tuple(bbox[i][0])
    #         point2 = tuple(bbox[(i+1) % n_lines][0])
    #         cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # exit(0)

    # //End5




