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

sim = init()
initBitString = getBitString(sim)

print('The map will be initialized with the following:', initBitString)

qr = QuantumRegister(16)
cr = ClassicalRegister(16)
qc = QuantumCircuit(qr, cr)

# # Map initialization and radomization
for i, bit in enumerate(initBitString):
	if (bit == '1'):
		qc.x(qr[i])
	qc.h(qr[i])


core_game(qc, qr, cr, sim)
# # Forcing map to get to previous state
# for i in range(qbits):
# 	qc.h(qr[i])
