from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit
qc = QuantumCircuit(2,2)

# Superposition
qc.h(0)

# Entanglement
qc.cx(0,1)

# Measurement
qc.measure([0,1],[0,1])

# Simulator
simulator = AerSimulator()

# Run experiment
job = simulator.run(qc, shots=1000)
result = job.result()

counts = result.get_counts()

print("Measurement results:", counts)

# Plot histogram
plot_histogram(counts)
plt.show()