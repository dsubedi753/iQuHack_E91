import socket, pickle
import json
from _thread import *
import random


def get_result(basis):
    print(basis.decode('utf-8'))
    # Stubb function for result
    return str(random.choice([0,1]))

def get_IP(connection):
    connection.sendall(str.encode(json.dumps(clientID)))

def threaded_client(connection, cl_num):
    # connection.send(str.encode(str(cl_num)))
    while True:
        data = connection.recv(1024)
        if not data:
            break
        if data.decode('utf-8') == "list":
            print("here")
            get_IP(connection)
        else:
            reply = get_result(data)
            connection.sendall(str.encode(reply))
    connection.close()


if __name__ == "__main__":
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 1233
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    
    print('Waitiing for a Connection..')
    ServerSocket.listen(5)
    clientID = dict()   
    
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        ThreadCount += 1
        clientID[ThreadCount] = (address[0], address[1],)
        start_new_thread(threaded_client, (Client,ThreadCount, ))
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


    