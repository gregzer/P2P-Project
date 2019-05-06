import Data
import LiveChating
import time

#To see when people send us a new message


def listen():
    for i in Data.new:
        if Data.dict[i][3] == "OFF":				#make sure that we are not already speaking to this personn
            print("[New_Message] Starting a new chat live because receive a new message")
            LiveChating.App(i)
            Data.new.remove(i)

def check_timer():
    while True:
        listen()
        time.sleep(2)                  #waiting 2 sec before updating


