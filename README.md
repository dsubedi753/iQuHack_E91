# E91 Quantum Key Distribution Network
Distributing Crypto Keys with QuTech hardware and an interface server
## Background

### Quantum Key Distribution

Suppose that User 1 wants to send a message to User 2. In order to protect the information in the message from the mediator, it must be encrypted. Encryption is the process of encoding the plaintext into ciphertext.The strength of encryption, that is, the property to resist decryption, is determined by its algorithm. Any encryption algorithm is based on the use of a key. Almost all contemporary encryption schemes rely on prime factorization, and Shor's algorithm can perform Prime factorization very efficiently, so this could lead to large security issue so for overcoming this a new way of encryption introduced called Quantum Key Distribution that uses Quantum Cryptograpy for the  encryption. 

Quantum Key Distribution uses the property of Quantum states collapsing the ability to measure in different basis 
<<<<<<< HEAD
to securely send a key, using a quantum and a classical channel, that can be used to communicate using the common 
encryption (like aes256) algorithms.

It achieves this by sending the key encoded in random basis and then, after the qubits have been measured, releasing the 
basis used as well as some parts of the sent key.

### E91
E91 was another Algorithm proposed for secure transmission of a key using a combination of a quantum and classical channel.
It uses works by sending two entangled particles (we'll use ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%7C%5Cpsi%5Crangle=%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D(%7C01%5Crangle&plus;%7C10%5Crangle))) 
to both Alice and Bob and measuring them in random basis. Alice can measure in the normal z-basis of ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5C%7B%7C0%5Crangle,%20%7C1%5Crangle%5C%7D) 
(called ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_1)) as well as that basis rotated by ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B4%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20a_2)) and ![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi) (![equation](https://latex.codecogs.com/svg.image?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cpi)) around the y-axis. 
Bob can measure in the z-basis rotated aroundd the y-axis by $\frac{1}{4}\pi$ ($b_1$), $\frac{1}{2}\pi$ ($b_2$) 
and $\frac{3}{4}\pi$ ($b_3$).
Alice and Bob then both release the Basis they used and compare where they used the same basis (the z-basis rotated 
around the same angle) and where they differed. The ones they agree on should have exactly opposite results. The ones
 where they differed validate the exchange.

### Validating E91 results
If we use $1$ and $-1$ as the results of our measurement instead of $1$ and $0$ and define $E(a_i, a_j)$ as the measured 
correlation, where $a_i$ and $a_j$ were the used basis, we can than use the following formula

![equation](https://latex.codecogs.com/svg.image?%5Cinline%20-2%5Csqrt%7B2%7D%5Cstackrel%7B?%7D%7B=%7DE(a_1,%20b_1)-E(a_1,b_3)&plus;E(a_3,b_1)&plus;E(a_3,b_3))

which is based on Bell's theorem to check, whether the communication was secure. The proper proof of this can be read 
in the original E91 Paper.

## Our Network
Our Network let's users connect to an interface server, which matches Users, who want to communicate. They then send 
their basis to the server, which contacts the Quantum Hardware by QuTech. The connection between user and server has
to be assumed to be secure, since the protocol is only as secure as it's weakest link. Sadly due to current limitations
this is the only way to do implement something similar on Quantum Hardware and in turn it is not viable in praxis yet.
=======
to securely send a key, using a quantum and a classical channel, that can be used to communicate using the common encryption (like aes256) algorithms.
It achieves this by sending the key encoded in random basis and then, after the qubits have been measured, releasing the basis used as well as some parts of the sent key.

### E91
E91 was another Algorithm proposed for secure transmission of a key using a combination of a quantum and classical channel.
It uses works by sending two entangled particles (we'll use <img src="https://render.githubusercontent.com/render/math?math=|\psi\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle">) to both Alice and Bob and measuring them in random basis. Alice can measure in the normal X-Basis of <img src="https://render.githubusercontent.com/render/math?math=\{|0\rangle, |1\rangle\}"> (called <img src="https://render.githubusercontent.com/render/math?math=a_1">) as well as that basis rotated by <img src="https://render.githubusercontent.com/render/math?math=\frac{1}{4}\pi"> (<img src="https://render.githubusercontent.com/render/math?math=a_2">) and <img src="https://render.githubusercontent.com/render/math?math=\frac{1}{2}\pi">(<img src="https://render.githubusercontent.com/render/math?math=a_3">). Bob can measure in the X-basis rotated by <img src="https://render.githubusercontent.com/render/math?math=\frac{1}{4}\pi"> (<img src="https://render.githubusercontent.com/render/math?math=b_1">), <img src="https://render.githubusercontent.com/render/math?math=\frac{1}{2}\pi"> (<img src="https://render.githubusercontent.com/render/math?math=b_2">) and <img src="https://render.githubusercontent.com/render/math?math=\frac{3}{4}\pi"> (<img src="https://render.githubusercontent.com/render/math?math=b_3">).
Alice and Bob then both release the Basis they used and compare where they used the same basis (the X-Basis rotated around the same angle) and where they differed. The ones they agree on should have exactly opposite results. The ones where they differed validate the exchange.

### Validating E91 results
If we use <img src="https://render.githubusercontent.com/render/math?math=1"> and <img src="https://render.githubusercontent.com/render/math?math=-1"> as the results of our measurement instead of <img src="https://render.githubusercontent.com/render/math?math=1"> and <img src="https://render.githubusercontent.com/render/math?math=0"> and define <img src="https://render.githubusercontent.com/render/math?math=E(a_i, a_j)"> as the measured correlation, where <img src="https://render.githubusercontent.com/render/math?math=a_i"> and <img src="https://render.githubusercontent.com/render/math?math=a_j"> were the used basis, we can than use the following formula

<img src="https://render.githubusercontent.com/render/math?math=-2\sqrt{2}\stackrel{?}{=}E(a_1, b_1)-E(a_1,b_3)+E(a_3,b_1)+E(a_3,b_3)">

which is based on Bell's theorem to check, whether the communication was secure. The proper proof of this can be read in the original E91 Paper.
>>>>>>> 05a583bbba9c1c2dc0b11444d8974f23bc63aade
