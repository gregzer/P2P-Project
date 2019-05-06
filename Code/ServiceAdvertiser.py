import socket
import Data
import time


#Announce his presence to the other ServiceListener in the network by sending json with info every x seconds(UDP)


def advertiser_timer():
    while True and Data.lever:
        run_advertiser()
        time.sleep(Data.SleepTime)                  #waiting x seconds before sending a new UDP(60 by default)



def run_advertiser():

        try:
            toServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #UDP
            toServer.connect((Data.UDP_Adverhost, Data.UDP_AdverPort))

            toServer.sendall((Data.ID_advertiser()).encode())

            print(Data.get_time(),"[ServiceAdvertiser] Closing of the connexion after sending informations")

            toServer.close()
        except:
            print(Data.get_time()+"[ServiceAdvertiser] couldn't connect to ip: \""+str(Data.UDP_Adverhost)+"\" and port: \""+ str(Data.UDP_AdverPort))+"\""









