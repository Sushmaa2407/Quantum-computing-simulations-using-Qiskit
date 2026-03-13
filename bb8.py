import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 20

alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)
bob_bases = np.random.randint(2, size=n)

simulator = AerSimulator()

bob_results = []

for i in range(n):

    qc = QuantumCircuit(1,1)

    if alice_bits[i] == 1:
        qc.x(0)

    if alice_bases[i] == 1:
        qc.h(0)

    if bob_bases[i] == 1:
        qc.h(0)

    qc.measure(0,0)

    job = simulator.run(qc, shots=1)
    result = job.result()

    counts = result.get_counts()

    measured_bit = int(list(counts.keys())[0])

    bob_results.append(measured_bit)

shared_key = []

for i in range(n):

    if alice_bases[i] == bob_bases[i]:
        shared_key.append(int(alice_bits[i]))

print("Alice bits:", alice_bits)
print("Bob results:", bob_results)
print("Shared secret key:", shared_key)