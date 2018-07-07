from colors import bcolors as color
from random import shuffle
from p_quantum import *
from core_game import *
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit,  available_backends, execute, get_backend
from qiskit.tools.visualization import plot_histogram
from qiskit import register, available_backends, get_backend

def go_measure(qc, qr, cr, sim):

	for i in range(16):
		qc.measure(qr[i], cr[i])

	backends = available_backends();
	backend = present_backends(sim, backends)

	if backend.status["available"] is True:
		stats = go_job(backend, qc, True, 1024)
		max = 0
		res = []
		# print('Stats :\n', stats)
		for bitString in stats:
			if (stats[bitString] > max):
				max = stats[bitString]
		for bitString in stats:
			if (stats[bitString] == max):
				res.append(bitString)
		print_map(res, max)
		return (1)
	else:
		print(color.FAIL, '  Backend', backend.name, 'is unavailable, try again later.', color.ENDC)

def is_gate(rec):
	gate = 0
	case = 0
	if (rec == 0):
		return (0)
	rec = rec.upper()
	rec = rec.split(' ')
	if (len(rec) > 3):
		print("WHY YOU TYPIN SO MUCH BRO ?")
		return (0)
	for i, s in enumerate(rec):
		if (i == 0):
			if (s != 'X' and s != 'Y' and s != 'Z'
			and s != 'T' and s != 'S' and s != 'SD'
			and s != 'H' and s != 'CX' and s != 'TD'
			and s!= 'SW'):
				print("Not a valid gate, please choose amongst : X, Y, Z, H, S, SDagger(SD), T, TDagger(TD), CNOT(CX), or Swap(SW)")
				return (0)
		if (i == 1 or i == 2):
			if (s.isdigit() == False or len(s) > 1 or (int(s) < 0 or int(s) > 15)):
				print("Not a valid case, please choose a number between 0 and 15")
				return (0)
	if (rec[0] == 'cx' or rec[0] == "SW"):
		if (len(rec) != 3):
			print("The", rec[0], "gate takes 2 arguments...")
			return (0)
		else:
			print('Applying gate', rec[0],'to case', rec[1], 'and', rec[2])
	else:
		print('Applying gate', rec[0], 'to case', rec[1])
	return (1)

def core_game(qc, qr, cr, sim):
	m = 0
	turn = 1
	while (m == 0):
		rec = 0
		while (is_gate(rec) == 0):

			rec = input("Player 1's turn: ") if (turn % 2 == 1) else input("Player 2's turn: ")
			if (rec == 'm' or rec == 'M'):
				print("Alright people ! Let the measurement begin !")
				return (go_measure(qc, qr, cr, sim))
		rec = rec.upper()
		rec = rec.split(' ')
		if (rec[0] == 'X'):
			qc.x(qr[int(rec[1])])
		if (rec[0] == 'Z'):
			qc.z(qr[int(rec[1])])
		if (rec[0] == 'Y'):
			qc.y(qr[int(rec[1])])
		if (rec[0] == 'SD'):
			qc.sdg(qr[int(rec[1])])
		if (rec[0] == 'TD'):
			qc.tdg(qr[int(rec[1])])
		if (rec[0] == 'T'):
			qc.t(qr[int(rec[1])])
		if (rec[0] == 'H'):
			qc.h(qr[int(rec[1])])
		if (rec[0] == 'S'):
			qc.s(qr[int(rec[1])])
		if (rec[0] == 'CX'):
			qc.cx(qr[int(rec[1])], qr[int(rec[2])])
		if (rec[0] == 'SW'):
			qc.cx(qr[int(rec[1])], qr[int(rec[2])])
			qc.cx(qr[int(rec[2])], qr[int(rec[1])])
			qc.cx(qr[int(rec[1])], qr[int(rec[2])])
		turn += 1
