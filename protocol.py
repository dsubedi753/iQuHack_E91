def establish_connection():  # True = Adam, False = Bob
    return True


def q_send_basis(basis):
    pass


def q_receive_result():
    pass


def c_send_basis(basis_arr):
    pass


def c_receive_basis():
    return []


def c_receive_decoy():
    return []


def c_send_decoy(decoy):
    pass


def e91protocol(bit_string_length, seed, rand_gen):
    role = establish_connection()
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
    return s+2*(2**0.5), key
