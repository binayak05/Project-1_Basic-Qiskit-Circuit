from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def run_circuit(qc):
    # Initialize simulator
    simulator = AerSimulator()
    
    # Run the quantum circuit
    job = simulator.run(qc, shots=1000)
    
    # Wait for the job to complete
    result = job.result()
    
    # Get the counts (measurement results)
    counts = result.get_counts(qc)
    return counts
