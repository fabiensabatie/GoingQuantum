# WHAT DOES THIS SCRIPT DO ?

import getpass, time, sys
from p_quantum import *
from core_game import *
from colors import bcolors as color
from random import shuffle
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from qiskit.tools.visualization import plot_histogram
from qiskit import register, available_backends, get_backend


# Initialization
sim = init()

# Map initialization thanks to a random 9bits long string obtained with a quantum circuit
initBitString = getBitString(sim)

qr = QuantumRegister(9)
cr = ClassicalRegister(9)
qc = QuantumCircuit(qr, cr)

# Map initialization and radomization
for i, bit in enumerate(initBitString):
	if (bit == '1'):
		qc.x(qr[i])
	qc.h(qr[i])

# Main run
print("Welcome to the Quantum Corewar, the game's principle is simple : Just like the\n\
regular tic-tac-toe, you have to align 3 O's or X's to win. The grid is represented by\n\
a 9 bits string, devided in 3 rows and 3 columns, to give a regular tic-tac-toe grid\n\
like this one:\n\n")
print("X  O  X\nX  X  O\nO  O  X\n\n");
print("You can apply gates to the qubits, ranging from 0 to 8. To apply a gate to the\n\
first qubit, the following command is 'H 0'. Some gates take two qubits like the CNOT\n\
gate. Once satisfied with your circuit, press 'm' or 'M' to measure the grid and know\n\
if you are the winner :D !")
core_game(qc, qr, cr, sim)
