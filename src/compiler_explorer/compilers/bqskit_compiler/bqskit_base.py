from compiler_explorer.compilers.base_compiler import BaseCompiler

from bqskit import compile, Circuit
from bqskit.ir.lang import get_language


class BqskitCompiler(BaseCompiler):
    def __init__(self) -> None:
        super().__init__()
    
    def placement(self, program, architecture=None, calibration=None):
        return super().placement(program, architecture, calibration)
    
    def routing(self, program, architecture=None, calibration=None):
        return super().routing(program, architecture, calibration)
    
    def optimisation(self, program, architecture=None, calibration=None):
        return super().optimisation(program, architecture, calibration)
    
    def optimal_compilation(self, program, architecture=None, calibration=None):
        language = get_language("qasm")
        bqskit_circuit = language.decode(program)

        compiled_circuit = compile(bqskit_circuit, optimization_level=1)
        language = get_language("qasm")
        return language.encode(compiled_circuit)