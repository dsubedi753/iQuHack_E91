# E91 Quantum Key Distribution Network
Distributing Encryption Keys with QuTech hardware and an interface server

## Abstract 
This project is prepared as submission to iQuHack 2022. This project implements the E91 Quantum Key Distrbution Algorithm. The network artichecture is constructed using Python's socket. The quantum computation and measurement is carried out by Quantum Inspire from QuTech. Due to limitation, such as lack of quantum channel, the project implements workaround with assumption that some parts of the communication, which are simulated to be quantum channel, are secured. The project is expanded for multiple users to join the network such that any two user would be able to request interface server for generating keys. An applet is designed for Graphical User Interface, where a client would be able to view all other client in the network and pair up with one to request for keys.

## Background

### Quantum Key Distribution

Encryption is the process of encoding the plaintext into ciphertext. This is used in various application ranging from storage to communication between the users. The strength of encryption, that is, the property to resist decryption, is determined by its algorithm. Any encryption algorithm is based on the use of one of more keys. Almost all contemporary encryption schemes rely on prime factorization, and Shor's algorithm can perform Prime factorization very efficiently, so this could lead to large security issue so for overcoming this a new way of encryption introduced called Quantum Key Distribution that uses Quantum Cryptograpy for the  encryption. 

Quantum Key Distribution algorithms leverages the property of quanntum mehcanics to securely produce a key, using a quantum and a classical channel. Most QKD algorithms uses the superposition of quantum states and the fact that measurement of such state produces prodicted or random result depending of bases used. The distributed key can be used to communicate using the common encryption algorithms like AES, SHA. The most popular protocol BB84 achieves this by one of the user sending superimposed qubits in random basis and then, after the qubits have been measured, releasing the basis used as well as some parts of the sent key for generation and validation of the key.

### E91
E91 was another Algorithm proposed for secure transmission of a key using a combination of a quantum and classical channel.
It uses works by sending two entangled particles (we'll use ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%7C%5Cpsi%5Crangle=%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D(%7C01%5Crangle&plus;%7C10%5Crangle))) 
to Alice and Bob and measuring them in random basis. Alice can measure in the normal z-basis of ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5C%7B%7C0%5Crangle,%20%7C1%5Crangle%5C%7D) 
(called ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_1)) as well as that basis rotated by ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_2)) and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_3)) around the y-axis. 
Bob can measure in the z-basis rotated aroundd the y-axis by ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_1)), ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_2)) 
and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B3%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_3)).
Alice and Bob then both release the Basis they used and compare where they used the same basis (the z-basis rotated 
around the same angle) and where they differed. The ones they agree on should have exactly opposite results. The ones
 where they differed validate the exchange.

### Validating E91 results
If we define ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20E(a_i,%20a_j)) as the measured 
correlation, where ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_i) and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_j) were the used basis, we can than use the following formula

![equation](https://latex.codecogs.com/svg.image?%5Cinline%20-2%5Csqrt%7B2%7D%5Cstackrel%7B?%7D%7B=%7DE(a_1,%20b_1)-E(a_1,b_3)&plus;E(a_3,b_1)&plus;E(a_3,b_3))

which is based on Bell's theorem to check, whether the communication was secure. The proper proof of this can be read in the original E91 Paper.

## Our Network
Our Network let's users connect to an interface server, which matches Users, who want to communicate. They then send their basis to the server. The interface server contacts the Quantum Hardware via QuTech. The connection between user and server has to be assumed to be secure, since the protocol is only as secure as it's weakest link. This communication tries to emulate the transfer of entangled bits to the users through a quantum channel. Sadly due to current limitations this is the only way to do implement something similar on Quantum Hardware and in turn it is not viable in pratice yet.

## Installation and Uses

### Dependencies 
- [Python](https://www.python.org/downloads/)
- [Qiskit](https://qiskit.org/)
- [Quantum Inspire](https://github.com/QuTech-Delft/quantuminspire#installation)

### Installaiton 
`git clone https://github.com/thunder753/iQuHack_E91.git`

### Running

1. Initiate Server
```python3 server_socket.py```

2. Run `gui.py` This is our client
3. Input the server IP `127.0.0.1` and port `1233`
4. Choose from one of the other clients to send the request
5. After request is accepted, keys can be generated with given parameters

<details><summary>Screenshots</summary>
<p>

![gui](https://user-images.githubusercontent.com/55018955/151708177-01a280ca-e866-460c-bc40-590c5ccfa216.png)
![gui2](https://user-images.githubusercontent.com/55018955/151708223-36f54448-dcda-4c70-9ab3-09f5cf9a07e4.png)


</p>
</details>

## References

- 
