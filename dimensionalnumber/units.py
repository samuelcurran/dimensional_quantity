from collections import namedtuple
from collections.abc import Mapping
from enum import Enum


class UnitsError(ArithmeticError):
    pass


class SiPrefix(Enum):
    E = 1e18
    P = 1e15
    T = 1e12
    G = 1e9
    M = 1e6
    k = 1e3
    h = 1e2
    da = 1e1
    d = 1e-1
    c = 1e-2
    m = 1e-3
    u = 1e-6
    n = 1e-9
    p = 1e-12
    f = 1e-15
    a = 1e-18


BaseUnits = namedtuple('BaseUnits', ('m', 'kg', 's', 'A', 'K', 'mol', 'cd'))


class Units(Mapping):
    def __init__(self, m=0, kg=0, s=0, A=0, K=0, mol=0, cd=0,
                 **kwargs) -> None:

        try:
            for power in (m, kg, s, A, K, mol, cd):
                if not float(power).is_integer():
                    raise UnitsError(
                            'Non-Integer Factor Of Units: {0}'.format(power))

            self._units = BaseUnits(
                    *(int(n) for n in (m, kg, s, A, K, mol, cd)))

            if kwargs:
                for unit, power in kwargs.items():
                    if not float(power).is_integer():
                        raise UnitsError(
                            'Non-Integer Factor Of Units: {0}'.format(power))
                    elif unit not in BaseUnits._fields:
                        raise UnitsError('Invalid Unit: {0}'.format(unit))

                self._units = self._units._replace(
                        **dict(((unit, int(power)) for (unit, power) in
                                kwargs.items())))
        except UnitsError as unit_err:
            raise unit_err
        except Exception as err:
            raise UnitsError(err)

    @property
    def units(self):
        return self._units._fields

    def __getitem__(self, key):
        return self._units._asdict().__getitem__(key)

    def get(self, key, default=None):
        return self._units._asdict().get(key, default)

    def __contains__(self, key):
        return self._units._asdict().__contains__(key)

    def keys(self):
        return self._units._asdict().keys()

    def items(self):
        return self._units._asdict().items()

    def values(self):
        return self._units._asdict().values()

    def __eq__(self, other):
        return self._units.__eq__(other)

    def __len__(self):
        return self._units.__len__()

    def __iter__(self):
        return self._units.__iter__()

    def __str__(self) -> str:
        return ':)'

    def __hash__(self) -> int:
        return self._units.__hash__()
