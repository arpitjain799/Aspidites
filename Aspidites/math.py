# cython: language_level=3, annotation_typing=True, c_string_encoding=utf-8
import sys
from warnings import warn
from typing import Any, Union
from inspect import getouterframes
try:
    from numpy import isinf, isnan, inf, nan
except ImportError:
    from math import inf, isinf, nan, isnan
finally:
    from math import factorial
import numbers
import numpy as np
from .api import Warn

Numeric = Union[int, float, complex, np.number]


class Undefined:
    """A monad for a failed programmatic unit; like NoneType but hashable.
    Falsy singleton acts as an absorbing element for division."""

    __slots__ = ("__weakref__", "__instance__", "func", "args", "kwargs")

    def __hash__(self):
        # noinspection PyUnresolvedReferences
        return hash(self.__weakref__)

    def __eq__(self, other: Any):
        return type(other) == Undefined

    def __add__(self, other: Any):
        return self

    def __sub__(self, other: Any):
        return self

    def __mul__(self, other: Any):
        return self

    def __truediv__(self, other: Any):
        return self

    def __floordiv__(self, other):
        return self

    def __neg__(self):
        return self

    def __invert__(self):
        return self

    def __str__(self):
        return self.__repr__()

    def __int__(self):
        return nan

    def __float__(self):
        return nan

    def __complex__(self):
        return complex(nan)

    def __oct__(self):
        return self

    def __index__(self):
        return 0

    def __len__(self):
        # Undefined has 0 elements
        return 0

    def __repr__(self):
        if hasattr(self.func, '__name__'):
            r = self.__class__.__name__ + f"({self.func.__name__}, {self.args}, {self.kwargs})"
        else:
            r = self.__class__.__name__ + f"({None}, {self.args}, {self.kwargs})"
        return r

    # noinspection PyMethodMayBeStatic
    def __nonzero__(self):
        return True

    def __init__(self, func=None, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


# noinspection PyPep8Naming,PyProtectedMember,PyUnresolvedReferences
def SafeFactorial(a: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    w: str
    stack: list
    exc: Exception
    if a < 0 or isnan(a) or isinf(a) or isinstance(a, (float, complex)):
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError(f"Factorial is Undefined for {a}")
        w = Warn(stack, stack[0][3], [a], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeFactorial, a)
    return factorial(a)


# noinspection PyPep8Naming,PyProtectedMember,PyUnresolvedReferences
def SafeUnaryAdd(a: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    w: str
    stack: list
    exc: Exception
    if isnan(a) or not isinstance(a, numbers.Number):
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError(f"Unary Add is Undefined for {type(a)}")
        w = Warn(stack, stack[0][3], [a], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeUnaryAdd, a)
    return +a


# noinspection PyPep8Naming,PyProtectedMember,PyUnresolvedReferences
def SafeUnarySub(a: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    w: str
    stack: list
    exc: Exception
    if isnan(a) or not isinstance(a, numbers.Number):
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError(f"Unary Sub is Undefined for {type(a)}")
        w = Warn(stack, stack[0][3], [a], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeUnarySub, a)
    return -a


# noinspection PyPep8Naming,PyProtectedMember,PyUnresolvedReferences
def SafeFloorDiv(a: Numeric, b: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    b: Numeric
    w: str
    stack: list
    exc: Exception
    if isinf(a) or b == 0 or (isinf(a) and isinf(b)):
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError("Division by zero is Undefined; this behavior diverges from IEEE 754-1985.")
        w = Warn(stack, stack[0][3], [a, b], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeFloorDiv, a, b)
    return a // b


# noinspection PyPep8Naming,PyProtectedMember,PyUnresolvedReferences
def SafeDiv(a: Numeric, b: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    b: Numeric
    w: str
    stack: list
    exc: Exception
    if b == 0 or (isinf(a) and isinf(b)):
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError("Division by zero is Undefined; this behavior diverges from IEEE 754-1985.")
        w = Warn(stack, stack[0][3], [a, b], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeDiv, a, b)
    return a / b


# noinspection PyPep8Naming, PyProtectedMember,PyUnresolvedReferences
def SafeMod(a: Numeric, b: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    b: Numeric
    w: str
    stack: list
    exc: Exception
    if isinf(a) or b == 0:
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError("Modulus by zero is Undefined; this behavior diverges from IEEE 754-1985.")
        w = Warn(stack, stack[0][3], [a, b], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeMod, a, b)
    return a % b


# noinspection PyPep8Naming, PyProtectedMember,PyUnresolvedReferences
def SafeExp(a: Numeric, b: Numeric) -> Union[Numeric, Undefined]:
    a: Numeric
    b: Numeric
    w: str
    stack: list
    exc: Exception
    # 0**0, inf**0, 0**inf
    if (a == 0 and b == 0) or (isinf(a) and b == 0) or (isinf(b) and a == 0):  # pragma: no cover
        stack = getouterframes(sys._getframe(0))
        exc = ArithmeticError(f"{str(a)}**{str(b)} == Undefined; this behavior diverges from IEEE 754-1985.")
        w = Warn(stack, stack[0][3], [a, b], {}).create(exc)
        warn(w, category=RuntimeWarning, stacklevel=0)
        return Undefined(SafeExp, a, b)
    try:
        return a ** b
    except OverflowError:
        return inf  # just a really big number on most systems
