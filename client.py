import socket, pickle
import random



def establish_connection():  # True = Adam, False = Bob
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    # Recieve the Client number
    cl_num = int(ClientSocket.recv(1024).decode('utf-8'))
    print("Welcome " + ("Adam" if cl_num == 1 else "Bob"))
    return cl_num == 1


def q_send_basis(basis):
    # Pickles the array and sends to int server
    ClientSocket.send(str.encode(str(basis)))



def q_receive_result():
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    return int(Response.decode('utf-8'))


def c_send_basis(basis_arr):
    # PSocket.send(pickle.dumps(basis_arr))))
    pass


def c_receive_basis():
    # data = PSocket.recv(4096)
    # basis = pickle.loads(data)
    return []


def c_receive_decoy():
    return []


def c_send_decoy(decoy):
    pass


def p2p_server():
    pass

def p2p_client():
    pass


def e91protocol(bit_string_length, seed, rand_gen):
    role = establish_connection()
    
    if role:
        p2p_server()
    else:
        p2p_client()
    
    rand_gen.seed(seed)
    basis_arr = []
    results_arr = []
    for _ in range(bit_string_length):
        basis_arr.append(rand_gen.choice([0, 1, 2] if role else [1, 2, 3]))
        q_send_basis(basis_arr[-1])
        results_arr.append(q_receive_result())
    c_send_basis(basis_arr)
    other_basis_arr = c_receive_basis()
    key = []
    decoy = []
    for (basis, other, result) in zip(basis_arr, other_basis_arr, results_arr):
        if basis == other:
            key.append(result)
        else:
            decoy.append(result)
    c_send_decoy(decoy)
    other_decoy = c_receive_decoy()
    s = 0
    for d in zip(decoy, other_decoy):
        s += (1 if d[0] == d[1] else -1)
    s = s/len(decoy)
    return s, key



if __name__ == "__main__":
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 1233
    
    PSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_p = '127.0.0.1'
    port_p = 1234
    
    establish_connection()
    q_send_basis(1)
    q_receive_result()
    
    # while True:
    #     Input = input('Say Something: ')
    #     ClientSocket.send(str.encode(Input))
    #     Response = ClientSocket.recv(1024)
    #     print(Response.decode('utf-8'))

    #e91protocol(20, 103942, random)
    
    ClientSocket.close()

