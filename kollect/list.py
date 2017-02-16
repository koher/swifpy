import typing as tp
import functools as ft
import builtins as py
from .optional import Optional

T = tp.TypeVar('T')
U = tp.TypeVar('U')


class List(tp.Generic[T]):
    def __init__(self, values: tp.Iterable[T]) -> None:
        self._values: tp.List[T] = py.list(values)

    def map(self, transform: tp.Callable[[T], U]) -> 'List[U]':
        return List(map(transform, self._values))

    def filter(self, is_included: tp.Callable[[T], bool]) -> 'List[T]':
        return List(filter(is_included, self._values))

    def flat_map(self, transform: tp.Callable[[T], 'List[U]']) -> 'List[U]':
        return self.map(lambda x: transform(x)).reduce(List[U]([]), lambda l, x: l + x)

    def reduce(self, initial: U, combine: tp.Callable[[U, T], U]) -> U:
        return ft.reduce(combine, self._values, initial)

    def for_each(self, body: tp.Callable[[T], None]) -> None:
        for value in self._values:
            body(value)

    def append(self, value: T) -> None:
        self._values.append(value)

    def get(self, index: int) -> Optional[T]:
        try:
            return Optional(self._values[index])
        except IndexError:
            return Optional(None)

    @property
    def first(self) -> Optional[T]:
        return self.get(0)

    @property
    def last(self) -> Optional[T]:
        return self.get(-1)

    @property
    def length(self) -> int:
        return self.__len__()

    def __iter__(self) -> tp.Iterator[T]:
        return self._values.__iter__()

    @tp.overload
    def __getitem__(self, index: int) -> T: pass

    @tp.overload
    def __getitem__(self, index: slice) -> 'List[T]': pass

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._values[key]
        elif isinstance(key, slice):
            return List(self._values[key])
        else:
            raise Exception('Never reaches here.')

    def __len__(self) -> int:
        return len(self._values)

    def __add__(self, other: 'List[T]') -> 'List[T]':
        return List(self._values + other._values)

    def __eq__(self, other: 'List[T]') -> bool:
        return self._values == other._values

    def __str__(self) -> str:
        return self._values.__str__()


def list(*values: T) -> List[T]:
    return List(values)
