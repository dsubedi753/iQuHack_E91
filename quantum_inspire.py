from qiskit import execute
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
from quantuminspire.credentials import get_authentication
from quantuminspire.qiskit import QI
import os
from math import pi
from quantuminspire.credentials import enable_account


enable_account('be6bdb84086d8b8cd1e69004f23717299b7d15b7')

QI_URL = os.getenv('API_URL', 'https://api.quantum-inspire.com/')

project_name = 'Enineone'
authentication = get_authentication()
QI.set_authentication(authentication, QI_URL, project_name=project_name)
qi_backend = QI.get_backend('QX single-node simulator')


def run_qi(bases_0, bases_1):
    measure_0 = []
    measure_1 = []

    for base_zero, base_one in zip(bases_0, bases_1):
        q = QuantumRegister(2)
        b = ClassicalRegister(2)
        circuit = QuantumCircuit(q, b)

        circuit.h(q[0])
        circuit.x(q[1])
        circuit.cx(q[0], q[1])

        circuit.ry(base_zero*pi/4, q[0])
        circuit.ry(base_one*pi/4, q[1])

        circuit.measure(q[0], b[0])
        circuit.measure(q[1], b[1])

        job = execute(circuit, backend=qi_backend, shots=1)
        result = job.result().get_counts(circuit)
        for state, counts in result.items():
            measure_0.append(int(state[0]))
            measure_1.append(int(state[1]))

    return measure_0, measure_1
