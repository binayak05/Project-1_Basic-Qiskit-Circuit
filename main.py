from circuit.build_circuit import build_circuit
from circuit.run_circuit import run_circuit

def main():
    qc = build_circuit()
    counts = run_circuit(qc)
    print(counts)

if __name__ == "__main__":
    main()
