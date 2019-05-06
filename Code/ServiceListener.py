import json
import Data
import socket

#Listening to all the UDP in the network in order to detect new users

def run_listener():

    print(Data.get_time() +"[ServiceListener] Turning ON and listening on port: "+str(Data.UDP_ListenPort))
    UDP_host = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((UDP_host, Data.UDP_ListenPort))

    while True and Data.lever:
        (data, addr) = s.recvfrom(128 * 1024)

        if not addr[0] in Data.BlockedList and  not Data.busy:			#Make sure that the ip is not blocked and the busy mode is OFF
            rcvMsg = data.decode()
            print(Data.get_time() + "[ServiceListener] Connected by" + str(addr)+ " with the message: " + str(rcvMsg) )

            if len(rcvMsg)>0and rcvMsg[0]=='{' and rcvMsg[len(rcvMsg)-1]=='}':
                    newuser(rcvMsg,addr[0])
            else:
                print(Data.get_time()+"[ServiceListener] Receving incorrect json message:"+ rcvMsg)

        else:
            print(Data.get_time()+"[ServiceListener] Blocked the connection of "+ addr[0])


def newuser(info,true_ip):
    try:
        info_parse = json.loads(info)   # handle wrong json

        if true_ip in Data.dict:        # if the ip is already stored in the dict, change the username if needed and the time off the last call

            x1=Data.dict[true_ip][2]
            y1=Data.dict[true_ip][3]
            Data.dict[true_ip]=info_parse.get("username"),Data.get_sec(),x1,y1

        else:
            Data.dict[true_ip] = info_parse.get("username"),Data.get_sec(),0,"OFF"  # new ip in the dict


        print(Data.get_time() +"[ServiceListener] Information: \"" + str(info_parse) +"\" added to the dictionnary")
    except:

        print(Data.get_time()+"[ServiceListener] Receive an incorrect UDP message: \""+ info +"\"")