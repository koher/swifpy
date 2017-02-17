import typing as tp
from .types import Bool, String

T = tp.TypeVar('T')
U = tp.TypeVar('U')


class Some(tp.Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    @property
    def x(self) -> T:  # `!` in Swift
        return self._value

    @tp.overload
    def qq(self, value: T) -> T: pass

    @tp.overload
    def qq(self, value: 'Optional[T]') -> 'Optional[T]': pass

    def qq(self, value):
        if isinstance(value, (Some, type(Nil))):  # temporary: does not work for nested optional values
            return self
        else:
            return self._value

    def map(self, transform: tp.Callable[[T], U]) -> 'Some[U]':
        return Some(transform(self._value))

    def flat_map(self, transform: tp.Callable[[T], 'Optional[U]']) -> 'Optional[U]':
        return transform(self._value)

    def __eq__(self, other: 'Optional[T]') -> Bool:
        if isinstance(other, Some):
            return self._value == other._value
        else:
            return False

    def __bool__(self):
        return True

    def __str__(self) -> String:
        return 'Optional(%s)' % self._value


class Nil:
    def __init__(self):
        pass

    @property
    def value(self) -> None:
        return None

    @property
    def x(self) -> T:
        raise NilError()

    @tp.overload
    def qq(self, value: T) -> T: pass

    @tp.overload
    def qq(self, value: 'Optional[T]') -> 'Optional[T]': pass

    def qq(self, value):
        return value

    def map(self, transform: tp.Callable[[T], U]) -> 'Nil':
        return self

    def flat_map(self, transform: tp.Callable[[T], 'Optional[U]']) -> 'Nil':
        return self

    def __eq__(self, other: 'Optional[T]') -> Bool:
        return not bool(other)

    def __bool__(self):
        return False

    def __str__(self) -> String:
        return 'Nil'


Optional = tp.Union[Some[T], Nil]

Nil = Nil()


class NilError(Exception):
    def __init__(self):
        super(NilError, self).__init__('Unexpectedly found none while unwrapping an Optional value.')


def optional(value: tp.Optional[T]) -> Optional[T]:
    if value:
        return Some(value)
    else:
        return Nil
