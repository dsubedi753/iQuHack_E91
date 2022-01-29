import random
import numpy as np


def establish_connection():  # True = Adam, False = Bob
    return True


def q_send_basis(basis):
    pass


def q_receive_result():
    pass


def c_send_basis(basis_string):
    pass


def c_receive_basis():
    return "01101010100011011010"


def e91protocol(bit_string_length, seed, rand_gen, error):
    role = establish_connection()
    rand_gen.seed(seed)
    basis_arr = []
    results_arr = []
    for _ in range(bit_string_length):
        basis_arr.append(rand_gen.choice([0, 1, 2] if role == "adam" else [1, 2, 3]))
        q_send_basis(basis_arr[-1])
        results_arr.append(q_receive_result())
    c_send_basis(basis_string)
    other_basis_string = c_receive_basis()
    key = []
    s = 0
    for b in zip(basis_string, other_basis_string):
        if b[0] == b[0]:
            key.append(results_arr)
        else:
            pass



if __name__ == "__main__":
    e91protocol(20, 103942, random)
