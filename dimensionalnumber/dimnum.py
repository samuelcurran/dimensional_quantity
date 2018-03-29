from dimensionalnumber.units import Units


class DimensionalNumber():

    def __init__(self, value, m=0, kg=0, s=0, A=0, K=0, mol=0, cd=0,
                 **kwargs):
        self._value = float(value)
        self._units = Units(*(m, kg, s, A, K, mol, cd), **kwargs)

    @property
    def value(self):
        return self._value

    @property
    def units(self):
        return self._units

    def __float__(self):
        return self._value

    def __divmod__(self, other):
        return super().__divmod__(other)

    def __rdivmod__(self, other):
        return super().__rdivmod__(other)

    def __floordiv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __sub__(self, other):
        return super().__sub__(other)

    def __rsub__(self, other):
        return super().__rsub__(other)

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __pow__(self, exponent):
        pass

    def __rpow__(self, base):
        pass

    def __abs__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
