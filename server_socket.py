import socket, pickle
import json
from _thread import *
import random
# import quantum_inspire


def get_result(basis):
    print(basis)
    # Stubb function for result
    return str(random.choice([0,1]))

def get_IP(connection):
    connection.sendall(pickle.dumps(list(clientID.values())));

def send_req(address, requester):
    requester_id = clientID[requester][0] +":"+ str(clientID[requester][1])
    found = False
    print(address[0])
    print(address[1])
    print("requester: " + requester_id)
    for key, value in clientID.items():
        if str(value[0]) == str(address[0]) and str(value[1]) == str(address[1]):
            found = True
            reqDict[key] = clientID[requester]
            break

def get_req(connection, cl_num):
    connection.sendall(pickle.dumps(reqDict[cl_num]))
    reqDict[cl_num] = None

def del_client(cl_num):
    clientID.pop(cl_num)

def threaded_client(connection, cl_num):
    # connection.send(str.encode(str(cl_num)))
    while True:
        data = connection.recv(1024)
        if not data:
            del_client(cl_num)
            break

        data = data.decode('utf-8')
        if data == "list":
            get_IP(connection)
        if data == "request":
            get_req(connection, cl_num)
        if "reqs" in data:
            target_add = data[5:]
            send_req(target_add.split(":"), cl_num)
        else:
            pass
            # reply = get_result(data)
            # connection.sendall(str.encode(reply))


    connection.close()


if __name__ == "__main__":
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = 'localhost'
    port = 1233
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    
    print('Waitiing for a Connection..')
    ServerSocket.listen(5)
    clientID = dict()   
    clientDict = dict()
    reqDict = dict()
    
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        Client.send(pickle.dumps((address[0], address[1],)))
        ThreadCount += 1
        clientID[ThreadCount] = (address[0], address[1], )
        reqDict[ThreadCount] = None
        start_new_thread(threaded_client, (Client,ThreadCount, ))
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


    