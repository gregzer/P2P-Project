import socket
import Data


#Send messages using TCP


def run_client(ip_to_connect_to,mess):


    print(Data.get_time() + "[Client] Turning ON")
    port = 5001

    try:
        toServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        toServer.connect((ip_to_connect_to, port))

        print(Data.get_time(),"[Client] Connexion set with server on the port {}".format(port))

        toServer.send(mess.encode())

        print(Data.get_time(),"[Client] Closing of the connexion after sending the message: \"" + mess +"\"")
        toServer.close()
        return True

    except:
       print (Data.get_time()+ "[CLIENT][WARNING] This ip is not avaible right now, the user disconnected or don't want you to connect")




