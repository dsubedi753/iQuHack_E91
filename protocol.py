import socket
import pickle


PORT = 1234


def q_establish_connection(server_addr, client_addr):  # True = Adam, False = Bob
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect(server_addr)
        print("yeah yeah")
    except socket.error as e:
        print(str(e))
    server_socket.send(str.encode(f"{client_addr[0]}:{client_addr[1]}"))
    role = int(server_socket.recv(1024).decode('utf-8')) == 1
    return server_socket, role


def q_send_basis(server_socket, basis):
    server_socket.send(str.encode(str(basis)))


def q_receive_result(server_socket):
    return int(server_socket.recv(1024).decode('utf-8')) == 1


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
            client_socket.connect(client_addr)
            return client_socket, None
    except socket.error as e:
        print(str(e))


def c_send_arr(connection, arr):
    connection.send(pickle.dumps(arr))


def c_receive_arr(connection):
    return pickle.loads(connection.recv(4096))


def e91protocol(bit_string_length, seed, rand_gen, server_addr, client_addr):
    server_socket, role = q_establish_connection(server_addr, client_addr)
    rand_gen.seed(seed)
    basis_arr = []
    results_arr = []
    for _ in range(bit_string_length):
        basis_arr.append(rand_gen.choice([0, 1, 2] if role else [1, 2, 3]))
        q_send_basis(server_socket, basis_arr[-1])
        results_arr.append(q_receive_result(server_socket))
    connection, client_socket = c_establish_connection(client_addr, (socket.gethostbyname(socket.gethostname()), PORT),
                                                       role)
    if role:
        c_send_arr(connection, basis_arr)
    other_basis_arr = c_receive_arr(connection)
    if not role:
        c_send_arr(connection, basis_arr)
    key = []
    decoy = []
    for (basis, other, result) in zip(basis_arr, other_basis_arr, results_arr):
        if basis == other:
            key.append(result)
        else:
            decoy.append(result)
    if role:
        c_send_arr(connection, decoy)
    other_decoy = c_receive_arr(connection)
    if not role:
        c_send_arr(connection, decoy)
    connection.close()
    if role:
        client_socket.close()
    s = 0
    for d in zip(decoy, other_decoy):
        s += (1 if d[0] == d[1] else -1)
    s = s/len(decoy)
    return s+2*(2**0.5), key
