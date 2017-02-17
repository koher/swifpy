import typing as tp
import functools as ft
import builtins as py
from .optional import Optional, optional
from .types import Bool, Int

T = tp.TypeVar('T')
U = tp.TypeVar('U')


def python_cmp(swift_cmp: tp.Callable[[T, T], Bool]) -> tp.Callable[[T, T], Int]:
    def cmp(x: T, y: T) -> Int:
        if swift_cmp(x, y):
            return -1
        elif x == y:
            return 0
        else:
            return 1
    return cmp


class Array(tp.Generic[T], tp.Iterable[T]):
    def __init__(self, values: tp.Iterable[T]) -> None:
        self._values: tp.List[T] = py.list(values)

    def map(self, transform: tp.Callable[[T], U]) -> 'Array[U]':
        return Array(map(transform, self._values))

    def filter(self, is_included: tp.Callable[[T], bool]) -> 'Array[T]':
        return Array(filter(is_included, self._values))

    def flat_map(self, transform: tp.Callable[[T], 'Array[U]']) -> 'Array[U]':
        return self.map(lambda x: transform(x)).reduce(Array[U]([]), lambda l, x: l + x)

    def reduce(self, initial: U, combine: tp.Callable[[U, T], U]) -> U:
        return ft.reduce(combine, self._values, initial)

    def for_each(self, body: tp.Callable[[T], None]) -> None:
        for value in self._values:
            body(value)

    def enumerated(self) -> 'Array[tp.Tuple[int, T]]':
        return Array(enumerate(self._values))

    def append(self, value: T) -> None:
        self._values.append(value)

    def insert(self, value: T, index: int) -> None:
        self._values.insert(index, value)

    def pop_last(self) -> Optional[T]:
        return optional(self._values.pop())

    def remove(self, index: int) -> T:
        return self._values.pop(index)

    def remove_all(self) -> None:
        self._values.clear()

    def sort(self, by: tp.Optional[tp.Callable[[T, T], Bool]] = None):
        if by:
            self._values.sort(key=ft.cmp_to_key(python_cmp(by)))
        else:
            self._values.sort()

    def sorted(self, by: tp.Optional[tp.Callable[[T, T], Bool]] = None) -> 'Array[T]':
        if by:
            return Array(sorted(self._values, key=ft.cmp_to_key(python_cmp(by))))
        else:
            return Array(sorted(self._values))

    def __get(self, index: int) -> Optional[T]:
        try:
            return optional(self._values[index])
        except IndexError:
            return optional(None)

    @property
    def first(self) -> Optional[T]:
        return self.__get(0)

    @property
    def last(self) -> Optional[T]:
        return self.__get(-1)

    @property
    def count(self) -> int:
        return self.__len__()

    def __iter__(self) -> tp.Iterator[T]:
        return self._values.__iter__()

    @tp.overload
    def __getitem__(self, index: int) -> T: pass

    @tp.overload
    def __getitem__(self, values: slice) -> 'Array[T]': pass

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._values[key]
        elif isinstance(key, slice):
            return Array(self._values[key])
        else:
            raise IndexError(str(key))

    @tp.overload
    def __setitem__(self, i: int, value: T) -> None: pass

    @tp.overload
    def __setitem__(self, s: slice, values: 'Array[T]') -> None: pass

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self._values[key] = value
        elif isinstance(key, slice):
            self._values[slice.start:slice.stop] = value
        else:
            raise IndexError(str(key))

    def __len__(self) -> int:
        return len(self._values)

    def __add__(self, other: 'Array[T]') -> 'Array[T]':
        return Array(self._values + other._values)

    def __eq__(self, other: 'Array[T]') -> bool:
        return self._values == other._values

    def __str__(self) -> str:
        return self._values.__str__()
