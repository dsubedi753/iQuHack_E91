import pickle
import socket
from _thread import *

import quantum_inspire


def get_ip(connection):
    connection.sendall(pickle.dumps(list(clientID.values())))


def send_req(address, requester, connection):
    found = False
    for key, value in clientID.items():
        if str(value[0]) == str(address[0]) and str(value[1]) == str(address[1]):
            found = True
            reqDict[key] = clientID[requester]
            break
    if found:
        connection.sendall(str.encode("sent"))
    else:
        connection.sendall(str.encode("error"))


def get_req(connection, cl_num):
    connection.sendall(pickle.dumps(reqDict[cl_num]))
    if reqDict[cl_num] is not None:
        ans = connection.recv(1024).decode("utf-8")
        acc = ans == "accept"
        for key, value in clientID.items():
            if str(value[0]) == str(reqDict[cl_num][0]) and str(value[1]) == str(reqDict[cl_num][1]):
                if acc:
                    clientDict[key].sendall(str.encode("accepted"))
                else:
                    clientDict[key].sendall(str.encode("rejected"))
                break
    

def del_client(cl_num):
    clientID.pop(cl_num)


def threaded_client(connection, cl_num):
    while True:
        data = connection.recv(1024)
        if not data:
            del_client(cl_num)
            break
        
        try:
            dat = data.decode('utf-8')
            # List the connected computers
            if dat == "list":
                get_ip(connection)
            # Check for any requests
            if dat == "request":
                get_req(connection, cl_num)
            # Make request
            if "reqs " in dat:
                target_add = dat[5:]
                send_req(target_add.split(":"), cl_num, connection)
        except ValueError:
            client_address, basis_0 = pickle.loads(data)
            for key, value in clientID.items():
                if str(value[0]) == str(client_address[0]) and str(value[1]) == str(client_address[1]):
                    _, basis_1 = pickle.loads(clientDict[key].recv(1024))
                    _, basis_1 = pickle.loads(clientDict[key].recv(4096))
                    measure_0, measure_1 = quantum_inspire.run_qi(basis_0, basis_1)
                    connection.sendall(pickle.dumps(measure_0))
                    clientDict[key].sendall(pickle.dumps(measure_1))
                    actual_ip_0 = connection.recv(1024).decode('utf-8')
                    actual_ip_1 = clientDict[key].recv(1024).decode('utf-8')
                    connection.sendall(str.encode(actual_ip_1))
                    clientDict[key].sendall(str.encode(actual_ip_0))
                    break
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
        Client.sendall(pickle.dumps((address[0], address[1],)))
        ThreadCount += 1
        clientID[ThreadCount] = (address[0], address[1], )
        reqDict[ThreadCount] = None
        clientDict[ThreadCount] = Client
        start_new_thread(threaded_client, (Client,ThreadCount, ))
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()
