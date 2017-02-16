# kollect

_kollect_ is a collection library for Python 3.6+ which has similar API to Swift and Kotlin.

```python
import kollect as k

numbers: k.List[int] = k.list(2, 3, 5)

second: int = numbers[1]      # 3
length: int = numbers.length  # 3

squared: k.List[int] = numbers.map(lambda x: x * x)            # [4, 9, 25]
odd: k.List[int] = numbers.filter(lambda x: x % 2 != 0)        # [3, 5]
sum: k.List[int] = numbers.reduce(0, lambda r, x: r + x)       # 10
twice: k.List[int] = numbers.flat_map(lambda x: k.list(x, x))  # [2, 2, 3, 3, 5, 5]
```

## Usage

### List

```python
import kollect as k

numbers: k.List[int] = k.list(2, 3, 5)

second: int = numbers[1]      # 3
length: int = numbers.length  # 3

squared: k.List[int] = numbers.map(lambda x: x * x)            # [4, 9, 25]
odd: k.List[int] = numbers.filter(lambda x: x % 2 != 0)        # [3, 5]
sum: k.List[int] = numbers.reduce(0, lambda r, x: r + x)       # 10
twice: k.List[int] = numbers.flat_map(lambda x: k.list(x, x))  # [2, 2, 3, 3, 5, 5]

first: k.Optional[int] = numbers.first  # Optional(2)
third: k.Optional[int] = numbers.last   # Optional(5)

for x in numbers:
    print(x)
```

### Optional

```python
import kollect as k

a: k.Optional[int] = k.some(2)
b: k.Optional[int] = k.some(3)
n: k.Optional[int] = k.none()

if a:
    print('Reaches here.')

if not n:
    print('Reaches here.')

squared1: k.Optional[int] = a.map(lambda x: x * x)                    # Optional(4)
squared2: k.Optional[int] = n.map(lambda x: x * x)                    # Optional()
sum1: k.Optional[int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)
sum2: k.Optional[int] = a.flat_map(lambda x: n.map(lambda y: x + y))  # Optional()

unwrapped = a.unwrapped
try:
    _ = n.unwrapped  # UnwrappingError
except k.UnwrappingError:
    print('Reaches here.')
```

## License

[The MIT License](LICENSE)
