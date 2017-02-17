import typing as tp

T = tp.TypeVar('T')
U = tp.TypeVar('U')


class Optional(tp.Generic[T], tp.Iterable[T]):
    def __init__(self, value: tp.Optional[T]) -> None:
        self._value: tp.Optional[T] = value

    @property
    def value(self) -> tp.Optional[T]:
        return self._value

    @property
    def unwrapped(self) -> T:
        if not self._value:
            raise UnwrappingError()
        return self._value

    def map(self, transform: tp.Callable[[T], U]) -> 'Optional[U]':
        if self._value:
            return Optional(transform(self._value))
        else:
            return Optional(None)

    def flat_map(self, transform: tp.Callable[[T], 'Optional[U]']) -> 'Optional[U]':
        if self._value:
            return transform(self._value)
        else:
            return Optional(None)

    def reduce(self, initial: U, combine: tp.Callable[[U, T], U]):
        if not self._value:
            return initial
        else:
            return combine(initial, self._value)

    def for_each(self, body: tp.Callable[[T], None]) -> None:
        if self._value:
            return body(self._value)

    @property
    def count(self) -> int:
        return self.__len__()

    def __iter__(self) -> tp.Iterator[T]:
        if self._value:
            return [self._value].__iter__()
        else:
            return [].__iter__()

    def __len__(self) -> int:
        if self._value:
            return 1
        else:
            return 0

    def __eq__(self, other: 'Optional[T]') -> bool:
        return self._value == other._value

    def __str__(self) -> str:
        if self._value:
            return 'Optional(%s)' % self._value
        else:
            return 'Optional()'


class UnwrappingError(Exception):
    def __init__(self):
        super(UnwrappingError, self).__init__('Unexpectedly found none while unwrapping an Optional value.')


def some(value: T) -> Optional[T]:
    return Optional(value)


def none() -> Optional[T]:
    return Optional(None)
