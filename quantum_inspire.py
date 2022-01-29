import os

from quantuminspire.credentials import enable_account
enable_account('YOUR_API_TOKEN')

from qiskit import execute
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit

from quantuminspire.credentials import get_authentication
from quantuminspire.qiskit import QI

QI_URL = os.getenv('API_URL', 'https://api.quantum-inspire.com/')


project_name = 'Qiskit-entangledd'
authentication = get_authentication()
QI.set_authentication(authentication, QI_URL, project_name=project_name)
qi_backend = QI.get_backend('QX single-node simulator')

q = QuantumRegister(2)
b = ClassicalRegister(2)
circuit = QuantumCircuit(q, b)

circuit.h(q[0])
circuit.cx(q[0], q[1])

qi_job = execute(circuit, backend=qi_backend, shots=256)
qi_result = qi_job.result()
histogram = qi_result.get_counts(circuit)
print('\nState\tCounts')
[print('{0}\t\t{1}'.format(state, counts)) for state, counts in histogram.items()]
# Print the full state probabilities histogram
probabilities_histogram = qi_result.get_probabilities(circuit)
print('\nState\tProbabilities')
[print('{0}\t\t{1}'.format(state, val)) for state, val in probabilities_histogram.items()]
