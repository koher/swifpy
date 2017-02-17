Swifpy
======

*Swifpy* makes Python Swifty. It provides some types which have similar
APIs with Swift's.

.. code:: python

    from swifpy import Array, Dictionary, Int, Optional, Some, String

    array: Array[Int] = Array([2, 3, 5])
    squared: Array[Int] = array.map(lambda x: x * x)  # [4, 9, 25]
    count: Int = array.count  # 3

    dictionary: Dictionary[String, Int] = Dictionary({'a': 2, 'b': 3, 'c': 5})
    a: Optional[Int] = dictionary['a']  # Optional(2)
    b: Optional[Int] = dictionary['b']  # Optional(3)

    sum: Optional[Int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)

Usage
-----

Bool, Float, Int, String
~~~~~~~~~~~~~~~~~~~~~~~~

They are just type aliases of ``bool``, ``float``, ``int`` and ``str``
respectivly.

Array
~~~~~

.. code:: python

    from swifpy import Array, Int, Optional, Some

    numbers: Array[Int] = Array([2, 3, 5])

    second: Int = numbers[1]    # 3
    count: Int = numbers.count  # 3

    squared: Array[Int] = numbers.map(lambda x: x * x)             # [4, 9, 25]
    odd: Array[Int] = numbers.filter(lambda x: x % 2 != 0)         # [3, 5]
    sum: Array[Int] = numbers.reduce(0, lambda r, x: r + x)        # 10
    twice: Array[Int] = numbers.flat_map(lambda x: Array([x, x]))  # [2, 2, 3, 3, 5, 5]

    first: Optional[Int] = numbers.first  # Optional(2)
    third: Optional[Int] = numbers.last   # Optional(5)

    for number in numbers:
        print(number)

Dictionary
~~~~~~~~~~

.. code:: python

    from swifpy import Dictionary, Int, Optional, Some, String

    dictionary: Dictionary[String, Int] = Dictionary({'a': 2, 'b': 3, 'c': 5})

    a: Optional[Int] = dictionary['a']  # Optional(2)
    dictionary['d'] = 7
    count: Int = dictionary.count  # 4

    for key, value in dictionary:
        print("%s -> %d" % (key, value))

Optional
~~~~~~~~

.. code:: python

    from swifpy import Int, Nil, Optional, Some, NilError

    a: Optional[Int] = Some(2)
    b: Optional[Int] = Some(3)
    n: Optional[Int] = Nil

    if a:
        print('Reaches here.')

    if not n:
        print('Reaches here.')

    squared1: Optional[Int] = a.map(lambda x: x * x)                    # Optional(4)
    squared2: Optional[Int] = n.map(lambda x: x * x)                    # Nil
    sum1: Optional[Int] = a.flat_map(lambda x: b.map(lambda y: x + y))  # Optional(5)
    sum2: Optional[Int] = a.flat_map(lambda x: n.map(lambda y: x + y))  # Nil

    unwrapped: Int = a.x  # `!` in Swift: `x` of e*x*clamation marks
    _ = n.x  # NilError

    # `??` in Swift: `q` of *q*uestion marks
    coalesced1: Int = a.qq(0)  ## 2
    coalesced2: Int = n.qq(0)  ## 0

License
-------

`The MIT License <LICENSE>`__
