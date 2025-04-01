import math
import cmath as cm
import numpy as np

class Phasor:
    def __init__(self, cplx):
        self.cplx = cplx

    @property
    def real(self):
        return self.cplx.real

    @property
    def imag(self):
        return self.cplx.imag

    @property
    def conj(self):
        return Phasor.polar(self.magnitude, -self.phase)

    @property
    def phase(self):
        return math.degrees(cm.phase(self.cplx))

    @property
    def magnitude(self):
        return abs(self.cplx)

    def __abs__(self):
        return self.magnitude

    def __str__(self):
        return f"Rectangular: {self.cplx.real:.3f} + j{self.cplx.imag:.3f}\nPolar: {abs(self.cplx):.3f} /_ {math.degrees(cm.phase(self.cplx)):.3f}{chr(176)}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Phasor.rect(self.cplx.real + other.cplx.real, self.cplx.imag + other.cplx.imag)
        else:
            return Phasor.rect(self.cplx.real + other, self.cplx.imag)

    def __radd__(self, lhs):
        return self + lhs

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Phasor.rect(self.cplx.real - other.cplx.real, self.cplx.imag - other.cplx.imag)
        else:
            return Phasor.rect(self.cplx.real - other, self.cplx.imag)

    def __rsub__(self, lhs):
        return -1*(self - lhs)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Phasor.polar(self.magnitude * other.magnitude, self.phase + other.phase)
        else:
            return Phasor.polar(self.magnitude * other, self.phase)

    def __rmul__(self, lhs):
        return self * lhs

    def __pow__(self, exp):
        return Phasor.polar(self.magnitude ** exp, self.phase * exp)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Phasor.polar(self.magnitude / other.magnitude, self.phase - other.phase)
        else:
            return Phasor.polar(self.magnitude / other, self.phase)

    def __rtruediv__(self, lhs):
        return Phasor.polar(lhs / self.magnitude, -self.phase)

    @classmethod
    def rect(cls, real, imag):
        return cls(cplx = complex(real, imag))

    @classmethod
    def polar(cls, magnitude, phase):
        return cls(cplx = cm.rect(magnitude, math.radians(phase)))
    
    @property
    def pf(self):
        return np.cos(cm.phase(self.cplx))

    @classmethod
    def power(cls, S, pf, mode):
        if mode == 'lagging' or mode == 'lag':
            return cls(cplx = cm.rect(S, np.arccos(pf)))
        elif mode == 'leading' or mode == 'lead':
            return cls(cplx = cm.rect(S, -np.arccos(pf)))
        else:
            raise Exception("Specify leading or lagging power factor!")



def ndprint(a):
    for r in a:
        print([str(v) for v in r])

j = Phasor.rect(0,1)
S = Phasor.power(10_000_000,0.9,'lead')/3
vr = 33/math.sqrt(3)
i = (S/vr).conj

Z = 1/j
#print(Z)

#print(Phasor.rect(15,10)-(2+2*j))
abcd = np.array([[1,Z],[0,1]])
vrir = np.array([0,2])
ndprint(abcd*vrir)


