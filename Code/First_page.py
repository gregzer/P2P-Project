import Server
import threading
import Data
import ServiceListener
import ServiceAdvertiser
import Main_Menu
import New_Message
from tkinter import *


def namefct(blaze,button,windows,label,error,errorlabel):

    if len(blaze.get())<3:
        error.set("Error while login in, please use more than 2 character in your username")  #we want more than 2 character in an username


    else:
        Data.ID["Username"] = blaze.get()                                                           #Saving username in a dict
        print(Data.get_time() ,"[Debug] Username taken:", (Data.ID).get("Username"))                #debug info

        errorlabel.destroy()
        label.destroy()
        blaze.destroy()
        button.destroy()


        threading.Thread(target=Server.run_serv).start()                            #running server
        threading.Thread(target=ServiceListener.run_listener).start()               #running listener
        threading.Thread(target=ServiceAdvertiser.advertiser_timer).start()         #running advertiser
        threading.Thread(target=New_Message.check_timer).start()					#running "New_message" to see when a user then a new message

        lo = Label(windows, text="Available users in the Network\n")
        lo.pack()

        Main_Menu.MainMenu(windows)
        #Mainmenu.main(windows)


def main():

    windows = Tk()
    windows.title('P2P PROJECT')

    windows.geometry("500x500")

    lo = Label(windows, text="\n\n\n\n\n\n\nPlease enter your name")
    lo.pack()

    Entryname = Entry(windows, bd =5)    #Username taker
    Entryname.pack()

    Bok = Button(windows, text="Log in", command=lambda: namefct(Entryname, Bok, windows, lo,error,errorlabel))
    Bok.pack()

    error = StringVar(windows)

    errorlabel=Label(windows, textvariable=error,fg="red")
    errorlabel.pack()

    print(Data.get_time(),"Programm turning ON")     #debug info
    windows.mainloop()


if __name__ == "__main__":
    # execute only if run as a script

    Data.dict={}
    main()