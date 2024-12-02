# quantum-compiler-explorer
Quantum Compiler Explorer

## Development plan


1. Build an initial qasm only comparing qiskit, bqskit and tket at the circuit level
2. Build timeline viewer for all the above
3. Expand scope to other compilers and language specs, notably QIR. Using Qbraid SDK where the native compiler doesn't support some language spec
4. Add support for different topologies and compiler options
5. Add gate highlighting, where did "x q[0];" on line 27 actually end up. Red if removed.
6. tart to build a hardware model zoo. That is, build out reference architectures for different quantum computing modalities to compile to
    - Start with fixed frequency superconducting reference architecture 
    - Build pulse viewer for this
7. Expand scope of reference models targeting, flux tunable superconducting, trapped ion, neutral atom (where circuit applies), quantum dot