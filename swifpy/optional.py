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

    def force_unwrapping(self) -> T:
        return self._value

    def map(self, transform: tp.Callable[[T], U]) -> 'Some[U]':
        return Some(transform(self._value))

    def flat_map(self, transform: tp.Callable[[T], 'Optional[U]']) -> 'Optional[U]':
        return transform(self._value)

    def __eq__(self, other: 'Optional[T]') -> Bool:
        if isinstance(other, Nil):
            return False
        else:
            return self._value == other._value

    def __str__(self) -> String:
        return 'Optional(%s)' % self._value


class Nil:
    def __init__(self):
        pass

    @property
    def value(self) -> None:
        return None

    def force_unwrapping(self) -> T:
        raise UnwrappingError()

    def map(self, transform: tp.Callable[[T], U]) -> 'Nil':
        return self

    def flat_map(self, transform: tp.Callable[[T], 'Optional[U]']) -> 'Nil':
        return self

    def __eq__(self, other: 'Optional[T]') -> Bool:
        return isinstance(other, Nil)

    def __str__(self) -> String:
        return 'Nil'


Optional = tp.Union[Some[T], Nil]


class UnwrappingError(Exception):
    def __init__(self):
        super(UnwrappingError, self).__init__('Unexpectedly found none while unwrapping an Optional value.')


def _optional(value: tp.Optional[T]) -> Optional[T]:
    if value:
        return Some(value)
    else:
        return Nil()