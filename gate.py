import sympy as sp
from functions import *

class QubitGate:
    def __init__(self):
        self.gate_type = None
        self.matrix = None
        self._SWAP = sp.Matrix([
            [1,0,0,0],
            [0,0,1,0],
            [0,1,0,0],
            [0,0,0,1],
        ])

class SingleQubitGate(QubitGate):
    def __init__(self):
        super().__init__()
        self.gate_type = "SingleQubitGate"

class TwoQubitGate(QubitGate):
    def __init__(self):
        super().__init__()
        self.gate_type = "TwoQubitGate"
    def get_submatrix(self, wire1, wire2):
        wire_min = min(wire1, wire2)
        wire_max = max(wire1, wire2)
        if wire_min + 1 == wire_max:
            if wire_min == wire1:
                return self.matrix
            elif wire_min == wire2:
                return self._SWAP * self.matrix * self._SWAP
        else:
            swap_gate = kron(identity(2**((wire_max-wire_min)-1)), self._SWAP)
            if wire_min == wire1:
                return swap_gate * kron(self.get_submatrix(wire_min, wire_max-1), identity(2)) * swap_gate
            elif wire_min == wire2:
                return swap_gate * kron(self.get_submatrix(wire_max-1, wire_min), identity(2)) * swap_gate

class H(SingleQubitGate):
    def __init__(self, wire):
        super().__init__()
        self.wire = wire
        self.matrix = (1/sp.sqrt(2)) * sp.Matrix([
            [1,1],
            [1,-1],
        ])

class X(SingleQubitGate):
    def __init__(self, wire):
        super().__init__()
        self.wire = wire
        self.matrix = sp.Matrix([
            [0,1],
            [1,0],
        ])

class Y(SingleQubitGate):
    def __init__(self, wire):
        super().__init__()
        self.wire = wire
        self.matrix = sp.Matrix([
            [0,-sp.I],
            [sp.I,0],
        ])

class Z(SingleQubitGate):
    def __init__(self, wire):
        super().__init__()
        self.wire = wire
        self.matrix = sp.Matrix([
            [1,0],
            [0,-1],
        ])

class RX(SingleQubitGate):
    def __init__(self, symbol_name, wire):
        super().__init__()
        self.symbol = sp.Symbol(symbol_name)
        self.wire = wire
        theta = self.symbol
        half  = sp.Rational(1, 2)
        self.matrix = sp.Matrix([
            [sp.cos(half*theta), -sp.I*sp.sin(half*theta)], 
            [-sp.I*sp.sin(half*theta), sp.cos(half*theta)], 
        ])

class RY(SingleQubitGate):
    def __init__(self, symbol_name, wire):
        super().__init__()
        self.symbol = sp.Symbol(symbol_name)
        self.wire = wire
        theta = self.symbol
        half  = sp.Rational(1, 2)
        self.matrix = sp.Matrix([
            [sp.cos(half*theta), -sp.sin(half*theta)], 
            [sp.sin(half*theta), sp.cos(half*theta)], 
        ])

class RZ(SingleQubitGate):
    def __init__(self, symbol_name, wire):
        super().__init__()
        self.symbol = sp.Symbol(symbol_name)
        self.wire = wire
        theta = self.symbol
        half  = sp.Rational(1, 2)
        self.matrix = sp.Matrix([
            [sp.exp(-sp.I*half*theta), 0], 
            [0, sp.exp(sp.I*half*theta)], 
        ])

class SWAP(TwoQubitGate):
    def __init__(self, wire1, wire2):
        super().__init__()
        self.wire1 = wire1
        self.wire2 = wire2
        self.matrix = sp.Matrix([
            [1,0,0,0],
            [0,0,1,0],
            [0,1,0,0],
            [0,0,0,1],
        ])
        self.submatrix = self.get_submatrix(wire1, wire2)

class CX(TwoQubitGate):
    def __init__(self, wire1, wire2):
        super().__init__()
        self.wire1 = wire1
        self.wire2 = wire2
        self.matrix = sp.Matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,1],
            [0,0,1,0],
        ])
        self.submatrix = self.get_submatrix(wire1, wire2)

class CZ(TwoQubitGate):
    def __init__(self, wire1, wire2):
        super().__init__()
        self.wire1 = wire1
        self.wire2 = wire2
        self.matrix = sp.Matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,-1],
        ])
        self.submatrix = self.get_submatrix(wire1, wire2)