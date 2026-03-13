from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit
qc = QuantumCircuit(1,1)

# Hadamard gate (superposition)
qc.ry(1.2,0)

# Measurement
qc.measure(0,0)

# Simulator
simulator = AerSimulator()

# Run experiment
job = simulator.run(qc, shots=1000)
result = job.result()

# Get counts
counts = result.get_counts()

print("Results:", counts)

# Plot histogram
plot_histogram(counts)

plt.show()