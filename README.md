# E91 Quantum Key Distribution Network
Distributing Crypto Keys with QuTech hardware and an interface server
## Background

### Quantum Key Distribution

Suppose that User 1 wants to send a message to User 2. In order to protect the information in the message from the mediator, it must be encrypted. Encryption is the process of encoding the plaintext into ciphertext.The strength of encryption, that is, the property to resist decryption, is determined by its algorithm. Any encryption algorithm is based on the use of a key. Almost all contemporary encryption schemes rely on prime factorization, and Shor's algorithm can perform Prime factorization very efficiently, so this could lead to large security issue so for overcoming this a new way of encryption introduced called Quantum Key Distribution that uses Quantum Cryptograpy for the  encryption. 

Quantum Key Distribution uses the property of Quantum states collapsing the ability to measure in different basis 

to securely send a key, using a quantum and a classical channel, that can be used to communicate using the common 
encryption (like aes256) algorithms.

It achieves this by sending the key encoded in random basis and then, after the qubits have been measured, releasing the 
basis used as well as some parts of the sent key.

### E91
E91 was another Algorithm proposed for secure transmission of a key using a combination of a quantum and classical channel.
It uses works by sending two entangled particles (we'll use ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%7C%5Cpsi%5Crangle=%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D(%7C01%5Crangle&plus;%7C10%5Crangle))) 
to both Alice and Bob and measuring them in random basis. Alice can measure in the normal z-basis of ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5C%7B%7C0%5Crangle,%20%7C1%5Crangle%5C%7D) 
(called ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_1)) as well as that basis rotated by ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_2)) and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi)) around the y-axis. 
Bob can measure in the z-basis rotated aroundd the y-axis by ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_1)), ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_2)) 
and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B3%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20b_3)).
Alice and Bob then both release the Basis they used and compare where they used the same basis (the z-basis rotated 
around the same angle) and where they differed. The ones they agree on should have exactly opposite results. The ones
 where they differed validate the exchange.

### Validating E91 results
If we define ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20E(a_i,%20a_j)) as the measured 
correlation, where ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_i) and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_j) were the used basis, we can than use the following formula

![equation](https://latex.codecogs.com/svg.image?%5Cinline%20-2%5Csqrt%7B2%7D%5Cstackrel%7B?%7D%7B=%7DE(a_1,%20b_1)-E(a_1,b_3)&plus;E(a_3,b_1)&plus;E(a_3,b_3))

which is based on Bell's theorem to check, whether the communication was secure. The proper proof of this can be read 
in the original E91 Paper.

## Our Network
Our Network let's users connect to an interface server, which matches Users, who want to communicate. They then send 
their basis to the server, which contacts the Quantum Hardware by QuTech. The connection between user and server has
to be assumed to be secure, since the protocol is only as secure as it's weakest link. Sadly due to current limitations
this is the only way to do implement something similar on Quantum Hardware and in turn it is not viable in praxis yet.
