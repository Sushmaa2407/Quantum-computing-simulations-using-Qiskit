import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 20

# Alice data
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)

# Eve chooses random bases
eve_bases = np.random.randint(2, size=n)

# Bob chooses random bases
bob_bases = np.random.randint(2, size=n)

simulator = AerSimulator()

bob_results = []

for i in range(n):

    qc = QuantumCircuit(1,1)

    # Alice encodes bit
    if alice_bits[i] == 1:
        qc.x(0)

    # Alice encodes basis
    if alice_bases[i] == 1:
        qc.h(0)

    # Eve measurement basis
    if eve_bases[i] == 1:
        qc.h(0)

    qc.measure(0,0)

    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()

    eve_result = int(list(counts.keys())[0])

    # Eve resends qubit
    qc = QuantumCircuit(1,1)

    if eve_result == 1:
        qc.x(0)

    if eve_bases[i] == 1:
        qc.h(0)

    # Bob measurement basis
    if bob_bases[i] == 1:
        qc.h(0)

    qc.measure(0,0)

    job = simulator.run(qc, shots=1)
    result = job.result()

    counts = result.get_counts()

    bob_bit = int(list(counts.keys())[0])

    bob_results.append(bob_bit)

# Key generation
shared_key = []
bob_key = []

for i in range(n):

    if alice_bases[i] == bob_bases[i]:

        shared_key.append(int(alice_bits[i]))
        bob_key.append(int(bob_results[i]))

# Calculate error rate
errors = 0

for i in range(len(shared_key)):
    if shared_key[i] != bob_key[i]:
        errors += 1

error_rate = errors / len(shared_key)

print("Alice bits:", alice_bits)
print("Alice bases:", alice_bases)
print("Eve bases:", eve_bases)
print("Bob bases:", bob_bases)

print("\nShared key (Alice):", shared_key)
print("Shared key (Bob):", bob_key)

print("\nError rate:", error_rate)