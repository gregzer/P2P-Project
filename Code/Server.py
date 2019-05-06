import socket
import select
import Data


#Listen for TCP connection. Will accept any one, unless the ip is blocked or the busy mode is ON



def run_serv():

    host = ""
    port = 5001
    main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_connexion.bind((host, port))
    main_connexion.listen(50)
    print(Data.get_time()+"[Server] Turning ON and listening on port 5001")

    server = True
    clients = []
    i = 0

    while server and Data.lever:

        asked_connexion, wlist, xlist = select.select([main_connexion], [], [], 0.05)

        for connexion in asked_connexion:

            toClient, info_connexion = connexion.accept()

            if not info_connexion[0]in Data.BlockedList and not Data.busy:		#make sure that the ip is not blocked and the busy mode is OFF

                print(Data.get_time(),'[Server] Connected by:', info_connexion)

                clients.append(toClient)
            else:
                print(Data.get_time()+"[Server] Blocked the connection of "+ info_connexion[0])

        clientToRead = []
        try:
            clientToRead, wlist, xlist = select.select(clients, [], [], 0.05)
        except select.error:
            pass
        else:

            for client in clientToRead:

                rcvMsg = client.recv(1024)
                rcvMsg = rcvMsg.decode()

                try:
                    f = open("log/"+str(info_connexion[0]) + ".txt", "r")
                    f.close()

                except FileNotFoundError:

                    f = open(str("log/"+info_connexion[0]) + ".txt", "w+")
                    f.close()


                f=open("log/"+str(info_connexion[0]) + ".txt", "a")
                try:
                    f.write(Data.get_time() + "["+str(Data.dict.get(info_connexion[0])[0])+"]" +": " +rcvMsg + "\n")
                except:
                    print(Data.get_time()+"[Server]nonetype is not subsciptable -> receved a message from someone that is not in the dict")
                f.close()


                if Data.dict[info_connexion[0]][3]=="OFF":
                    Data.new.append(info_connexion[0])

                print(Data.get_time() +"[Server] Receive the message: \"" + rcvMsg +"\" from: "+ str(Data.dict.get(info_connexion[0])[0]) + " with the ip: "+ str(info_connexion[0]))


                clientToRead.remove(client)
                clients.remove(client)


    print(Data.get_time() + "[Server] Closing of the connexion")
    for client in clients:
        client.close()

    main_connexion.close()
    print(Data.get_time()+"[Server]Turning OFF")

