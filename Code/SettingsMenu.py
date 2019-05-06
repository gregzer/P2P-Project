import Data
from tkinter import *
import Main_Menu

#Menu to change almost all the variable in the app.


class Settings():

    def __init__(self):

        self.root= Tk()
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        self.L1 = Label(self.root, text="MyIP:")
        self.L1.place(x=100, y=10)
        self.E1 = Entry(self.root, bd=5)
        self.E1.insert(0,Data.myip)
        self.E1.place(x=180, y=10)

        self.L2 = Label(self.root, text="Advertising on the IP:")
        self.L2.place(x=50, y=50)
        self.E2 = Entry(self.root, bd=5)
        self.E2.insert(0,Data.UDP_Adverhost)
        self.E2.place(x=180, y=50)

        self.L3 = Label(self.root, text="Advertising on port:")
        self.L3.place(x=50, y=90)
        self.E3 = Entry(self.root, bd=5)
        self.E3.insert(0,Data.UDP_AdverPort)
        self.E3.place(x=180, y=90)

        self.L4 = Label(self.root, text="My name:")
        self.L4.place(x=50, y=130)
        self.E4 = Entry(self.root, bd=5)
        try:
            self.E4.insert(0, Data.ID["Username"])
        except:
            print(Data.get_time()+"settingsmenu error, name not readable because not in the dict")   #if name not in the dict
        self.E4.place(x=180, y=130)


        self.L5 = Label(self.root, text="Manualy add someone to the dictionary")
        self.L5.place(x=0, y=170)

        self.L6 = Label(self.root, text="Username:")
        self.L6.place(x=0, y=195)
        self.E6 = Entry(self.root, bd=5)
        self.E6.place(x=70, y=195)

        self.L7 = Label(self.root, text="IP:")
        self.L7.place(x=220, y=195)
        self.E7 = Entry(self.root, bd=5)
        self.E7.place(x=240, y=195)

        self.B1 = Button(self.root, text="Add", command=lambda:Settings.DictAdd(self))
        self.B1.place(x=390, y=195)

        self.L8 = Label(self.root, text="Block the connexion off the ip:")
        self.L8.place(x=0, y=250)
        self.E8 = Entry(self.root, bd=5)
        self.E8.place(x=200, y=250)

        self.Bip = Button(self.root, text="Block", command=lambda: Settings.BlockIp(self))
        self.Bip.place(x=330, y=250)

        self.L8 = Label(self.root, text="Unblock the ip:")
        self.L8.place(x=0, y=290)
        self.E9 = Entry(self.root, bd=5)
        self.E9.place(x=200, y=290)

        self.Bip2 = Button(self.root, text="Unblock", command=lambda: Settings.UnBlockIp(self))
        self.Bip2.place(x=330, y=290)

        self.Ltime = Label(self.root, text="Time between each advertisement:")
        self.Ltime.place(x=0, y=320)
        self.Etime = Entry(self.root, bd=5)
        self.Etime.insert(0, Data.SleepTime)
        self.Etime.place(x=200, y=320)

        self.c = Checkbutton(self.root, text="Busy mode", variable=Data.busy,onvalue=True, offvalue=False,command= lambda:self.Checkbutton())
        self.c.place(x=190,y=400)
        if Data.busy==True:
            self.c.select()

        self.B2 = Button(self.root, text="Clean Dictionnary", command=lambda: Settings.Cleandict(self))
        self.B2.place(x=190, y=430)

        self.B3 = Button(self.root, text="Save changes",command=lambda:Settings.save(self))
        self.B3.place(x=200, y=460)

        self.root.mainloop()

    def Checkbutton(self):

        if Data.busy==False:
            Data.busy=True
            print(Data.get_time()+"[SettingsMenu] Busy mode ON")
        else:
            Data.busy=False
            print(Data.get_time()+"[SettingsMenu] Busy mode OFF")

    def UnBlockIp(self):

        try:
            Data.BlockedList.remove(self.E9.get())
            print(Data.get_time()+"[SettingsMenu]UnBlocking the ip: " + self.E9.get())
            self.E9.delete(0, END)
        except:
            print(Data.get_time()+"[SettingsMenu][WARNING] Trying to unblock an ip that is not blocked")

    def BlockIp(self):

        print(Data.get_time()+"[SettingsMenu]Blocking the ip: "+ self.E8.get())
        Data.BlockedList.insert(0,self.E8.get())
        self.E8.delete(0, END)


    def save(self):

        Data.myip=self.E1.get()
        Data.UDP_Adverhost=self.E2.get()
        Data.UDP_AdverPort=int(self.E3.get())
        Data.SleepTime=int(self.Etime.get())

        if len(self.E4.get())>2:
            Data.ID["Username"]=self.E4.get()
        self.root.destroy()


    def DictAdd(self):
        try:
            if len(self.E7.get())>6 and len(self.E6.get())>0:
                Data.dict[self.E7.get()] = self.E6.get(), Data.get_sec(), 0, "OFF"
                print(Data.get_time()+"[SettingMenu] Added the ip: \"" + str(self.E7.get()) + "\" with the username: \"" + str(self.E6.get()) + "\" in the Dictionnary")
                self.E6.delete(0,END)
                self.E7.delete(0, END)

        except:
            print(Data.get_time()+"[SettingsMenu] Error while trying to manually add someone to the dict")
        print(Data.dict)


    def Cleandict(self):

        for i in Main_Menu.Liste:
            try:
                    i[0].destroy()
                    Main_Menu.ipListe.remove(i[1])

            except:
                print(Data.get_time()+"[SettingsMenu]error, must have deleted the dict")

        self.root.update()
        Main_Menu.Liste=[]
        Data.dict={}








