import socket
import time


# File to store variables and functions

lever=True

SleepTime=60					#Time between each advertissement

new=[]							#Liste of ip that sent a new message

busy=False                      # check if the users is busy or not

dict = {}                       # The dict used to store users ip, username, numbers of new message, and see if the livechat is open

BlockedList=[]                  #List of blocked ip

UDP_Adverhost = "192.168.1.255" #ip used by the advertiser

UDP_AdverPort=5001              # port used by the advertiser

UDP_ListenPort=5001             #port used by the Listener

ID={}                           #Personnal information, username

local_time = time.ctime(time.time())  #actual time in sec

myip=socket.gethostbyname(socket.gethostname())   #my ip


def Blockedusers():             #return all the blocked ip
    lm=""
    for i in BlockedList:
        lm= lm +" "+i
    return lm

def ID_advertiser():

    return "{\"username\": \""+ str(ID.get("Username")) + "\", \"ip_address\": \""+ myip+"\"}"          #json for UDP advertiser


def get_sec():
    return time.time()


def get_time():

    return "["+time.ctime(time.time())[11:19]+"]"


def is_connected():

    try:
        socket.create_connection(("www.google.com", 80))                #try a connection to google
        return(True)
    except OSError:
        pass
    return (False)


