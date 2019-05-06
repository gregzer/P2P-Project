from tkinter import *
import Data
import ServiceAdvertiser
import LiveChating
import SettingsMenu



#Main Menu of the application


Liste=[]
ipListe=[]

class MainMenu():


    def __init__(self,windows):

        self.windows=windows
        self.windows.protocol("WM_DELETE_WINDOW", lambda: MainMenu.closing(self))

        for ip in Data.dict:

            if (int(Data.get_sec()) - Data.dict[ip][1]) < 61:

                self.Bok = Button(windows, text=Data.dict[ip][0],command=lambda ip=ip: LiveChating.App(ip))
                self.Bok.config(height=1, width=40)
                self.Bok.pack()

                Liste.append((self.Bok,ip))
                ipListe.append(ip)

                self.windows.update()

        self.Bt_ClientListe = Button(windows, text="Informations on the network", command=lambda:MainMenu.clientListe(self))
        self.Bt_ClientListe.config(height=1, width=40)
        self.Bt_ClientListe.pack(side=BOTTOM)

        self.Bt_Settings = Button(windows, text="Settings menu", command=lambda: SettingsMenu.Settings())
        self.Bt_Settings.config(height=1, width=40)
        self.Bt_Settings.pack(side=BOTTOM)

        self.update_clock()

        self.windows.mainloop()





    def update_clock(self):
        global ipListe
        global Liste
        for i in Liste:
            try:
                if (Data.get_sec()- Data.dict[i[1]][1])>62:

                    i[0].destroy()
                    ipListe.remove(i[1])
                    Liste.remove(i)

            except:
                print(Data.get_time()+"[Main_Menu]error, must have deleted the dict")

        try:
            for ip in Data.dict:

                if (int(Data.get_sec()) - Data.dict[ip][1]) < 61 and ip not in ipListe:

                    self.Bok = Button(self.windows, text=Data.dict[ip][0],command=lambda ip=ip: LiveChating.App(ip))
                    self.Bok.config(height=1, width=40)
                    self.Bok.pack()

                    Liste.append((self.Bok,ip))
                    ipListe.append(ip)

                    self.windows.update()

        except:
            print(Data.get_time()+"[Main_Menu]error in dict handled")
        self.windows.update()
        self.windows.after(1000, self.update_clock)


    def closing(self):
        Data.lever=False
        self.windows.destroy()

    def clientListe(self):

        windows = Tk()
        windows.title('P2P PROJECT')
        windows.geometry("750x750")
        text = Text(windows, height=50, width=100)

        text.configure(state='normal')
        if Data.is_connected():
            text.insert(CURRENT, "Connected to internet= YES\n")
        else:
            text.insert(CURRENT, "Connected to internet= NO\n")

        text.insert(CURRENT, "Numbers of users: " + str(len(Data.dict)) + "\n")
        text.insert(CURRENT, "My ip: " + str(Data.myip) + "\n")
        text.insert(CURRENT, "My name: " + str(Data.ID["Username"]) + "\n\n")

        for x, y in Data.dict.items():

            text.insert(CURRENT, "ip: " + str(x) + " Name: " + str(y[0]) + "       Last call : " + str(
                int(Data.get_sec() - y[1])) + " seconds " + "\n")

        text.insert(CURRENT, "\nBlocked users: " + Data.Blockedusers() + "\n\n")
        text.configure(state='disabled')  # So the user can't write in the textbox
        text.pack()
        print(Data.get_time(), "[Interface] Main_Menu Interface ON")

        windows.mainloop()



