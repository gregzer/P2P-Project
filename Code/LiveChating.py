from tkinter import *
import time
import Data
import Client


#Used when starting a chat with someone


class App():

    def closing(self):

        print("[LiveChat] Chat windows with: \"" + str(Data.dict[self.ip][0]) + "\" closed")
        x1 = Data.dict[self.ip][0]
        y1 = Data.dict[self.ip][1]
        z1 = Data.dict[self.ip][2]
        Data.dict[self.ip] = x1,y1,z1,"OFF"  # setting the state in dict to"OFF so we know that we are not speaking anymore with that ip"

        self.state="OFF"
        self.root.after(1000, lambda:self.root.destroy())    #add to wait 1000ms to avoid error because off the "after" still trying to acces the deleted root


    def send_message(self,mess,Entry_mess):

        if len(mess) > 0 and Client.run_client(self.ip, mess):      # message must be correctly sent and can't be empty

            Entry_mess.delete(0, END)  # if the message is sent without error, deleting the message in the text zone
            f = open("log/"+self.ip + ".txt", "a")
            f.write(Data.get_time() + mess + "\n")
            f.close()


    def __init__(self,ip):

        x = Data.dict[ip][0]
        y = Data.dict[ip][1]
        Data.dict[ip] = x, y, 0,"ON"           #saying that the chat with this ip is currently open

        self.ip=ip
        self.root = Tk()

        self.state="ON"
        self.label = Label(self.root,text="Chatting with: "+ Data.dict[ip][0], anchor='w', justify='left',font = "Arial 10 bold italic")
        self.label.pack()
        self.root.geometry("500x500")

        self.root.protocol("WM_DELETE_WINDOW", lambda: App.closing(self))
        self.Entry_mess = Entry(self.root, bd=5)
        self.Entry_mess.pack(side=BOTTOM)

        self.Bt_send = Button(self.root, text="Send message",command=lambda:App.send_message(self,self.Entry_mess.get(),self.Entry_mess) )
        self.Bt_send.pack(side=BOTTOM)

        self.update_clock()

        self.root.mainloop()



    def update_clock(self):

        try:
            f = open("log/"+self.ip + ".txt", "r")

        except FileNotFoundError:

            f = open("log/"+self.ip + ".txt", "w+")


        lines = f.readlines()
        nbr = len(lines)
        now=""
        po = 0

        while po < nbr:             #printing the last 25 lines in the interface
            if po >= nbr - 25:
                now+=lines[po]
            po += 1

        f.close()

        if self.state == "ON":
            self.label.configure(text=now)
            self.root.after(1000, self.update_clock)



