from types import NotImplementedType

from sympy.plotting.intervalmath.interval_arithmetic import interval

def Abs(x) -> interval: ...
def exp(x) -> interval: ...
def log(x) -> interval: ...
def log10(x) -> interval: ...
def atan(x) -> interval: ...
def sin(x) -> interval: ...
def cos(x) -> interval: ...
def tan(x) -> interval | NotImplementedType: ...
def sqrt(x) -> interval: ...
def imin(*args) -> type[NotImplementedError] | interval: ...
def imax(*args) -> type[NotImplementedError] | interval: ...
def sinh(x) -> interval: ...
def cosh(x) -> interval: ...
def tanh(x) -> interval: ...
def asin(x) -> interval | None: ...
def acos(x) -> interval | None: ...
def ceil(x) -> interval | type[NotImplementedError]: ...
def floor(x) -> interval | type[NotImplementedError]: ...
def acosh(x) -> interval | type[NotImplementedError]: ...
def asinh(x) -> interval | type[NotImplementedError]: ...
def atanh(x) -> interval | type[NotImplementedError]: ...
def And(*args) -> tuple[bool | None, bool | None]: ...
def Or(*args) -> tuple[bool | None, bool | None]: ...