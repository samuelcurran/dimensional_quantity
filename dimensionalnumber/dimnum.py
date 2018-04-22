from collections import namedtuple, OrderedDict
from itertools import repeat
from numbers import Number
from operator import add, floordiv, mul, sub, truediv

from util import seq_equal, zipmap

SI_UNITS = ('m', 'kg', 's', 'A', 'K', 'mol', 'cd')
Units = namedtuple('Units', SI_UNITS)


class DimensionalQuantity(Number):
    def __init__(self, scalar, m=0, kg=0, s=0, A=0, K=0, mol=0, cd=0,
                 **kwargs):
        try:
            self._scalar = float(scalar)
        except ValueError:
            raise ValueError(
                "Non-numeric type given for dimensional quantity: {0}".format(
                    scalar))

        units = OrderedDict((('m', m), ('kg', kg), ('s', s), ('A', A),
                             ('K', K), ('mol', mol), ('cd', cd)))
        units.update(kwargs)

        for k, v in units.items():
            if k not in SI_UNITS:
                raise ValueError("Invalid unit given: {0}".format(k))
            try:
                if isinstance(v, int):
                    continue
                elif float(v).is_integer():
                    units[k] = int(v)
                    continue
            except ValueError:
                raise ValueError("Non-numeric factors of {0}: {1}".format(
                    k, v))
            else:
                raise ValueError("Non-integer factors of {0}: {1}".format(
                    k, v))

        self._units = Units(*units.values())

    def __str__(self):
        return "{0} {1}".format(self._scalar, "".join([
            "{0}{1}".format(unit, dim)
            for unit, dim in self._units._asdict().items() if dim != 0
        ]))

    #=========================================================================
    #          Numeric Methods
    #=========================================================================

    def __add__(self, other):
        if isinstance(other, DimensionalQuantity):
            if seq_equal(self._units, other._units):
                return DimensionalQuantity(self._scalar + other._scalar, *self._units)
            else:
                raise ValueError("Cannot add unequal types")
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, DimensionalQuantity):
            if seq_equal(self._units, other._units):
                return DimensionalQuantity(self._scalar - other._scalar, *self._units)
            else:
                raise ValueError("Cannot add unequal types")
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return DimensionalQuantity(self._scalar * other, *self._units)
        elif isinstance(other, DimensionalQuantity):
            return DimensionalQuantity(self._scalar * other._scalar,
                          *zipmap(add, self._units, other._units))
        else:
            raise NotImplementedError

    def __matmul__(self, other):
        raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return DimensionalQuantity(self._scalar / other, *self._units)
        elif isinstance(other, DimensionalQuantity):
            return DimensionalQuantity(self._scalar / other._scalar,
                          *zipmap(sub, self._units, other._units))
        else:
            raise NotImplementedError

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return DimensionalQuantity(self._scalar // other, *self._units)
        elif isinstance(other, DimensionalQuantity):
            return DimensionalQuantity(self._scalar // other._scalar,
                          *zipmap(sub, self._units, other._units))
        else:
            raise NotImplementedError

    def __mod__(self, other):
        raise NotImplementedError

    def __divmod__(self, other):
        raise NotImplementedError

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return DimensionalQuantity(self._scalar**other,
                          *zipmap(mul, self._units, repeat(other, 7)))
        else:
            raise NotImplementedError

    def __lshift__(self, other):
        raise NotImplementedError

    def __rshift__(self, other):
        raise NotImplementedError

    def __and__(self, other):
        raise NotImplementedError

    def __xor__(self, other):
        raise NotImplementedError

    def __or__(self, other):
        raise NotImplementedError

    #=========================================================================
    #          Reflexive Numeric Methods
    #=========================================================================

    def __radd__(self, other):
        raise NotImplementedError

    def __rsub__(self, other):
        raise NotImplementedError

    def __rmul__(self, other):
        raise NotImplementedError

    def __rmatmul__(self, other):
        raise NotImplementedError

    def __rtruediv__(self, other):
        raise NotImplementedError

    def __rfloordiv__(self, other):
        raise NotImplementedError

    def __rmod__(self, other):
        raise NotImplementedError

    def __rdivmod__(self, other):
        raise NotImplementedError

    def __rpow__(self, other):
        raise NotImplementedError

    def __rlshift__(self, other):
        raise NotImplementedError

    def __rrshift__(self, other):
        raise NotImplementedError

    def __rand__(self, other):
        raise NotImplementedError

    def __rxor__(self, other):
        raise NotImplementedError

    def __ror__(self, other):
        raise NotImplementedError

    #=========================================================================
    #          In-place Numeric Methods
    #=========================================================================

    def __iadd__(self, other):
        raise NotImplementedError

    def __isub__(self, other):
        raise NotImplementedError

    def __imul__(self, other):
        raise NotImplementedError

    def __imatmul__(self, other):
        raise NotImplementedError

    def __itruediv__(self, other):
        raise NotImplementedError

    def __ifloordiv__(self, other):
        raise NotImplementedError

    def __imod__(self, other):
        raise NotImplementedError

    def __idivmod__(self, other):
        raise NotImplementedError

    def __ipow__(self, other):
        raise NotImplementedError

    def __ilshift__(self, other):
        raise NotImplementedError

    def __irshift__(self, other):
        raise NotImplementedError

    def __iand__(self, other):
        raise NotImplementedError

    def __ixor__(self, other):
        raise NotImplementedError

    def __ior__(self, other):
        raise NotImplementedError

    #=========================================================================
    #          Unary Numeric Methods
    #=========================================================================

    def __neg__(self):
        raise NotImplementedError

    def __pos__(self):
        raise NotImplementedError

    def __abs__(self):
        raise NotImplementedError

    def __invert__(self):
        raise NotImplementedError

    def __complex__(self):
        raise NotImplementedError

    def __int__(self):
        raise NotImplementedError

    def __float__(self):
        return self._scalar

    def __index__(self):
        raise NotImplementedError

    def __round__(self):
        raise NotImplementedError

    def __trunc__(self):
        raise NotImplementedError

    def __floor__(self):
        raise NotImplementedError

    def __ceil__(self):
        raise NotImplementedError
