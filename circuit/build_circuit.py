from qiskit import QuantumCircuit

def build_circuit():
    qc = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
    qc.h(0)                   # Apply Hadamard gate to put qubit into superposition
    qc.measure(0, 0)           # Measure qubit into classical bit
    return qc
