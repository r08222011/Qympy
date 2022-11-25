# Qympy - Quantum Analytic Computation with Sympy
A sympy based python package for symbolic calculation of $n$-qubit quantum state.
See GitHub: https://github.com/r08222011/Qympy

---

### Get Started

**1. Circuit Initialization**
Common circuits ansatz can be found in `/src/qympy/quantum_circuit`. To build a circuit from beginning, use `sp_circuit.Circuit`. The basic use of `Circuit` is same as [Qiskit](https://qiskit.org). For example:
```python3
>>> from sp_circuit import Circuit

>>> num_qubits = 2  # Number of qubits in the circuit
>>> qc = Circuit(2) # Initialize a two-qubit circuit
>>> qc.h(0)         # Apply Hadamard Gate at qubit 0
>>> qc.cx(0,1)      # Apply CNOT gate with control 0 and target 1
```

1. Draw the circuit
We now have initialized a quantum circuit. To see the circuit we built, we can use `Circuit.draw()`. This method use [qiskit.circuit.QuantumCircuit.draw](https://qiskit.org/documentation/stubs/qiskit.circuit.QuantumCircuit.draw.html) with `draw('mpl')` as default. For example:
```python3
>>> qc.draw("mpl")
```
![plot](./src/qympy/example/example_readme.png)

1. Evolve and measure the circuit
The last step for getting the analytic expression is to call the method `Circuit.evolve_state()`. This will calculate the final state with the gates applied. After evolving the quantum state, we can measure the quantum state with *X*, *Y*, *Z* basis with a single certain qubit. For example:
```python3
>>> qc.evolve_state()
>>> qc.measure(0, "X")
>>> sp.latex(qc.measure(0, "X"))
'2 \\sin{\\left(\\frac{t_{0}}{2} \\right)} \\cos{\\left(\\frac{t_{0}}{2} \\right)}'
```
Note, you can see the prettier expression with [jupyter](https://jupyter.org).

---

### License

MIT License

Copyright (c) 2022 Yi-An Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.