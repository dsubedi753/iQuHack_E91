import socket, pickle
import os
from _thread import *
import random


def get_reply(data):
    # Stubb function for reply
    basis = pickle.loads(data)
    print(repr(basis))
    return 'Server Says: Hello'

def get_result(basis):
    # Stubb function for result
    print(basis.decode('utf-8'))
    return str(random.choice([0,1]))


def threaded_client(connection, cl_num):
    connection.send(str.encode(str(cl_num)))
    while True:
        data = connection.recv(1024)
        if not data:
            break
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
    
    
    
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        ThreadCount += 1
        start_new_thread(threaded_client, (Client,ThreadCount, ))
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


    