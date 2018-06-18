import getpass, time, sys
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from qiskit.tools.visualization import plot_histogram
from qiskit import register, available_backends, get_backend
import matplotlib.pyplot as plt
plt.rc('font', family='monospace')

def plot_smiley (stats, shots):
	for bitString in stats:
		char = chr(int( bitString[0:8] ,2)) # get string of the leftmost 8 bits and convert to an ASCII character
		char += chr(int( bitString[8:16] ,2)) # do the same for string of rightmost 8 bits, and add it to the previous character
		prob = stats[bitString] / shots # fraction of shots for which this result occurred
		# create plot with all characters on top of each other with alpha given by how often it turned up in the output
		plt.annotate( char, (0.5,0.5), va="center", ha="center", color = (0,0,0, prob ), size = 300)
		if (prob>0.05): # list prob and char for the dominant results (occurred for more than 5% of shots)
			print(str(prob)+"\t"+char)
	plt.axis('off')
	plt.show()

APItoken = getpass.getpass('Please enter your API token (https://quantumexperience.ng.bluemix.net/qx/account/advanced): ')
qx_config = {
	"APItoken": APItoken,
	"url":"https://quantumexperience.ng.bluemix.net/api"
}
try:
	register(qx_config['APItoken'], qx_config['url'])
except:
	print('Something went wrong.\nIs the token correct?')

# set up registers and program
qr = QuantumRegister(16)
cr = ClassicalRegister(16)
qc = QuantumCircuit(qr, cr)

# rightmost eight (qu)bits have ')' = 00101001
qc.x(qr[0])
qc.x(qr[3])
qc.x(qr[5])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[9]) # create superposition on 9
qc.cx(qr[9],qr[8]) # spread it to 8 with a CNOT
qc.x(qr[11])
qc.x(qr[12])
qc.x(qr[13])

# measure
for j in range(16):
	qc.measure(qr[j], cr[j])

print('The following backends are available, please select one: ')
backends = available_backends();
backends.sort()
print('\n\033[92m###### Quantum Computers: ######\033[0m')
print('IBMQX5 has 16 QBits - IBMQX4 and IBMQX2 have 5 QBits')
for idx, backend in enumerate(backends):
	if backend.find('ibmqx') == 0:
		print(backend,'(',idx,')')

print('\n\033[92m########## Simulators ##########\033[0m')
for idx, backend in enumerate(backends):
	if backend.find('ibmqx'):
		print(backend,'(',idx,')')
input = input()
backend = get_backend(backends[int(input)])
print('Status of', backends[int(input)], ':', backend.status)
if backend.status["available"] is True:
	print('Submitting the job to backend ', backends[int(input)])
	shots_device = 1000
	job_device = execute(qc, backend, shots=shots_device)
	stats_device = job_device.result().get_counts()
else:
	print("\nThe device is not available. Try again later.")
plot_smiley(stats_device, shots_device)

sys.exit()
