import os
from math import pi

from quantuminspire.credentials import enable_account
enable_account('YOUR_API_TOKEN')

from qiskit import execute
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit

from quantuminspire.credentials import get_authentication
from quantuminspire.qiskit import QI

QI_URL = os.getenv('API_URL', 'https://api.quantum-inspire.com/')

project_name = 'Enineone'
authentication = get_authentication()
QI.set_authentication(authentication, QI_URL, project_name=project_name)
qi_backend = QI.get_backend('QX single-node simulator')

alice_bases = '1111111111'
bob_bases = '1111111111'
alice_measure = []
bob_measure = []

for i in range(len(alice_bases)):
    q = QuantumRegister(2)
    b = ClassicalRegister(2)
    circuit = QuantumCircuit(q, b)

    circuit.h(q[0])
    circuit.cx(q[0], q[1])
    circuit.x(q[1])
    
    if alice_bases[i] == '0':
        circuit.ry(-pi/2,q[0])
    elif alice_bases[i] == '1':
        circuit.ry(-pi/4,q[0])
    if bob_bases[i] == '1':
        circuit.ry(-pi/4,q[1])
    elif bob_bases[i] == '3':
        circuit.ry(pi/4,q[1])
        
    #circuit.measure(q[0], b[0])
    #circuit.measure(q[1], b[1])

    job = execute(circuit, backend=qi_backend, shots=1)
    result = job.result().get_counts(circuit)
    for state, counts in result.items():
        alice_measure.append(state[1])
        bob_measure.append(state[0])
