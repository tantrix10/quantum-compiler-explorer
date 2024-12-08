from compiler_explorer.compilers.base_compiler import BaseCompiler

from pytket.passes import FullPeepholeOptimise, RebaseTket
from pytket.qasm import circuit_from_qasm_str, circuit_to_qasm_str

class TketCompiler(BaseCompiler):
    def __init__(self) -> None:
        super().__init__()
    
    def placement(self, program, architecture=None, calibration=None):
        return super().placement(program, architecture, calibration)
    
    def routing(self, program, architecture=None, calibration=None):
        return super().routing(program, architecture, calibration)
    
    def optimisation(self, program, architecture=None, calibration=None):
        return super().optimisation(program, architecture, calibration)
    
    def optimal_compilation(self, program, architecture=None, calibration=None):
        tket_circuit = circuit_from_qasm_str(program)
        tket_circuit = RebaseTket().apply(tket_circuit)
        tket_circuit = FullPeepholeOptimise().apply(tket_circuit)
        return circuit_to_qasm_str(tket_circuit)
