import socket
import pickle
import ipaddress


PORT = 1234


def own_ip():
    return socket.gethostbyname(socket.gethostname())


def q_establish_connection(server_addr):
    try:
        ipaddress.ip_address(server_addr[0])
        ip = server_addr[0]
    except ValueError:
        ip = socket.gethostbyname(server_addr[0])
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        pass
        server_socket.connect((ip, server_addr[1]))
        own_addr = pickle.load(server_socket.recv(4096).decode())
    except socket.error as e:
        own_addr = None
        print(str(e))
    return server_socket, own_addr


def q_update(server_socket):
    server_socket.send(str.encode("list"))
    client_list = pickle.load(server_socket.recv(4096).decode())
    server_socket.send(str.encode("request"))
    requests = pickle.load(server_socket.recv(4096).decode())
    requests = None if requests[0] is None else requests
    return client_list, requests


def q_choose_user(server_socket, client_addr):
    pass


def c_establish_connection(client_addr, own_addr, role):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if role:
            client_socket.bind(own_addr)
            while True:
                client_socket.listen(1)
                connection, address = client_socket.accept()
                if address != client_addr:
                    connection.close()
                else:
                    break
                return connection, client_socket
        else:
            client_socket.connect((client_addr[0], PORT,))
            return client_socket, None
    except socket.error as e:
        print(str(e))


def send_arr(connection, arr):
    connection.send(pickle.dumps(arr))


def receive_arr(connection):
    return pickle.loads(connection.recv(4096))


def e91protocol(bit_string_length, seed, rand_gen, server_socket, role, client_addr):
    rand_gen.seed(seed)
    basis_arr = []
    for _ in range(bit_string_length):
        basis_arr.append(rand_gen.choice([0, 1, 2] if role else [1, 2, 3]))
    send_arr(server_socket, basis_arr)
    results_arr = receive_arr(server_socket)
    connection, client_socket = c_establish_connection(client_addr, (own_ip(), PORT), role)
    if role:
        send_arr(connection, basis_arr)
    other_basis_arr = receive_arr(connection)
    if not role:
        send_arr(connection, basis_arr)
    key = []
    decoy = []
    for (basis, other, result) in zip(basis_arr, other_basis_arr, results_arr):
        if basis == other:
            key.append(result)
        else:
            decoy.append(result)
    if role:
        send_arr(connection, decoy)
    other_decoy = receive_arr(connection)
    if not role:
        send_arr(connection, decoy)
    connection.close()
    if role:
        client_socket.close()
    s = 0
    for d in zip(decoy, other_decoy):
        s += (1 if d[0] == d[1] else -1)
    s = s/len(decoy)
    return s+2*(2**0.5), key
