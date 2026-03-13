from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit_aer.noise import NoiseModel, depolarizing_error
import matplotlib.pyplot as plt

# Quantum circuit
qc = QuantumCircuit(1,1)

qc.h(0)

qc.measure(0,0)

# Ideal simulation
simulator = AerSimulator()

job = simulator.run(qc, shots=1000)

result = job.result()

ideal_counts = result.get_counts()

print("Ideal result:", ideal_counts)

# Create noise model
noise_model = NoiseModel()

error = depolarizing_error(0.1, 1)

noise_model.add_all_qubit_quantum_error(error, ['h'])

# Noisy simulation
noisy_sim = AerSimulator(noise_model=noise_model)

job = noisy_sim.run(qc, shots=1000)

result = job.result()

noisy_counts = result.get_counts()

print("Noisy result:", noisy_counts)

# Plot comparison
plot_histogram([ideal_counts, noisy_counts],
               legend=['Ideal','Noisy'])

plt.show()