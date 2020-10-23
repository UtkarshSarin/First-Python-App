import Backend
import Scan
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Welcome to Sarins Cinema")
choice = IntVar()


timing1 = Radiobutton(window,text='Book New Ticket', value=1, variable=choice)

timing2 = Radiobutton(window,text='Scan Existing Ticket', value=2, variable=choice)

timing3 = Radiobutton(window,text='Quit App', value=3, variable=choice)




lbl = Label(window, text="Hey, What do you feel like doing right now?")

lbl.grid(column=0, row=1)
timing1.grid(column=0, row=2)

timing2.grid(column=0, row=3)

timing3.grid(column=0, row=4)


def click():
    if(choice.get() == 1):
        print("iamhere")
        Backend.BookMovie()
        
    elif(choice.get() == 2):
        Scan.video_reader()
    else:
        exit(0)

btn = Button(window, text="Book", command=click)
btn.grid(column=0, row=9)
window.mainloop()




    
        