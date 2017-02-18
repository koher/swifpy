import typing as tp
from .optional import Optional, optional, String

K = tp.TypeVar('K')
V = tp.TypeVar('V')


class Dictionary(tp.Generic[K, V], tp.Iterable[tp.Tuple[K, V]]):
    @tp.overload
    def __init__(self, entries: tp.Dict[K, V]) -> None: pass

    @tp.overload
    def __init__(self, entries: tp.Iterable[tp.Tuple[K, V]]) -> None: pass

    def __init__(self, entries) -> None:
        self._entries: tp.Dict[K, V] = dict(entries)

    def __getitem__(self, key: K) -> Optional[V]:
        return optional(self._entries.get(key))

    def __setitem__(self, key: K, value: V) -> None:
        self._entries[key] = value

    @property
    def keys(self) -> tp.Iterable[K]:
        return self._entries.keys()

    @property
    def values(self) -> tp.Iterable[V]:
        return self._entries.values()

    def for_each(self, body: tp.Callable[[K, V], None]) -> None:
        for key, value in self._entries.items():
            body(key, value)

    @property
    def count(self) -> int:
        return len(self._entries)

    def remove_all(self) -> None:
        self._entries.clear()

    def __iter__(self) -> tp.Iterator[tp.Tuple[K, V]]:
        return self._entries.items().__iter__()

    def __repr__(self) -> String:
        return repr(self._entries)

