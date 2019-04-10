import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
# Import Aer
from qiskit import BasicAer

qBits = 2

# Create a Quantum Register with qBits qubits.
q = QuantumRegister(qBits, 'q')
# Create a Classical Register with qBits bits.
c = ClassicalRegister(qBits, 'c')
# Create a Quantum Circuit acting on the q register
circ = QuantumCircuit(q, c)
# Add a H gate on qubit 0, putting this qubit in superposition.

for qBit in q:
	circ.x(qBit)


# DJ Algo
for qBit in q:
	circ.h(qBit)

# Constant function
#for qBit in q:
#	circ.x(qBit)

# Balanced function

# DJ Algo
for qBit in range(0, qBits - 1):
	circ.h(q[qBit])

circ.measure(q,c)
# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = execute(circ, backend_sim, shots=1)

# Grab the results from the job.
result_sim = job_sim.result()
counts = result_sim.get_counts(circ)
print(counts)
