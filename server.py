
import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()

        playerName=player_socket.recv(1024).decode().strip()

        if (len(CLIENTS.keys())==0) :
            CLIENTS[playerName]={"playerType":"player1"}
        else :
            CLIENTS[playerName]={"playerType":"player2"}
            
        CLIENTS[playerName]["playerSocet"]= player_socket
        CLIENTS[playerName]["playeraddr"]= addr
        CLIENTS[playerName]["player_Name"]=playerName
        CLIENTS[playerName]["player_Turn"]=True

        print(f" CONNECTION established with {playerName} : {addr}")
        print(CLIENTS)

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()