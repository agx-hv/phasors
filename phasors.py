import math
import cmath as cm
import numpy as np

class Phasor:
    def __init__(self, cplx):
        self.cplx = cplx

    @property
    def phase(self):
        return math.degrees(cm.phase(self.cplx))

    @property
    def magnitude(self):
        return abs(self.cplx)

    def __str__(self):
        return f"Rectangular: {self.cplx.real:.3f} + j{self.cplx.imag:.3f}\nPolar: {abs(self.cplx):.3f} /_ {math.degrees(cm.phase(self.cplx)):.3f}{chr(176)}"

    def __add__(self, other):
        return Phasor.new_rect(self.cplx.real + other.cplx.real, self.cplx.imag + other.cplx.imag)

    def __sub__(self, other):
        return Phasor.new_rect(self.cplx.real - other.cplx.real, self.cplx.imag - other.cplx.imag)

    def __mul__(self, other):
        return Phasor.new_polar(self.magnitude * other.magnitude, self.phase + other.phase)

    def __truediv__(self, other):
        return Phasor.new_polar(self.magnitude / other.magnitude, self.phase - other.phase)

    @classmethod
    def new_rect(cls, real, imag):
        return cls(cplx = complex(real, imag))

    @classmethod
    def new_polar(cls, magnitude, phase):
        return cls(cplx = cm.rect(magnitude, math.radians(phase)))

class PowerTriangle:
    def __init__(self, P, pf, direction="lagging"):
        S_magnitude = P/pf
        angle = np.arccos(pf) if direction="lagging" else -np.arccos(pf)
        self.phasor = Phasor.new_polar(S_magnitude)

v1 = Phasor.new_polar(1,45)
v2 = Phasor.new_rect(0,1)

print(v1*v2)

