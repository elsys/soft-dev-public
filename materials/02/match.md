---
theme: default
class: 
    - lead
    - invert
paginate: true
---
# **Python: Structural Pattern Matching**

- new in python 3.10 (released on 04.10.2021)

---
# **Syntax**
<br>

~~~python
match <expression>:
    case <pattern> <guard>:
        <code block to be executed>
    case <pattern> <guard>:
        <code block to be executed>
    ...
~~~
<br>

- no fallthrough
- ```__eq__``` is used for comparisons
- ```match``` and ```case``` are soft keywords

---
# **Literal pattern**

``` literal_pattern: number | string | Boolean | None ```
- switch functionality
<br>

~~~python
match number:
    case 7:
        print("Seven!")
    case 2.71:
        print("e")
    case 2+1j:
        print("Complex number!")
~~~

---
# **Capture pattern**

```capture_pattern: NAME```
- target assignment for the matched expression
- a name can be bound once in a pattern
<br>

~~~python
match name:
    case "":
        print("Invalid name")
    case employee:
        print(f"Hi {employee}")

print(employee)  # Doesn't raise NameError if case employee matches
~~~

---
# **Wildcard Pattern**

 - ```wildcard_pattern: '_'```
 - doesn't bind
 - can be used as many times as desired

~~~python
 match weather:
    case "sunny":
        print("Nice weather")
    case "rainy":
        print("Bad weather")
    case _:  # always matches (if nothing else matches)
        print(f"The weather is {_}")  # NameError (Not a capture pattern! Can't bind)
~~~

---
# **Constant Value Pattern**

``` constant_pattern: NAME ('.' NAME)+ ```
- must be a qualified (dotted) name
- used for matching against constants and enums
- never binds

~~~python
import enum

class Colours(enum.Enum):
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ...

match soil.colour:
    case Colours.RED:  # checks if soil.colour == Colours.RED
        print("the climate must be warm!")
    case colour:  # capture pattern
        print(f"Colour: {colour} soil")
~~~

---
# **Sequence Pattern**

- similar to list/tuple unpacking
- elements nested within can be any kind of patterns, not just names or sequences
- subject must be an instance of [collections.abc.Sequence](https://docs.python.org/3/glossary.html#term-sequence) or have a [Py_TPFLAGS_SEQUENCE](https://docs.python.org/3/c-api/typeobj.html#Py_TPFLAGS_SEQUENCE) bit set

~~~python
match collection:
    case 1, [x, *others]:
        print("Got 1 and a nested sequence")
    case (1, x):
        print(f"Got 1 and {x}")
~~~

- [*_ ] matches a sequence of any length
- (_ , _ , *_) matches any sequence of length two or more
- ["a", *_, "z"] matches any sequence of length two or more that starts with "a" and ends with "z"

---
# **Mapping Pattern**

- generalization of iterable unpacking to [mappings](https://docs.python.org/3/glossary.html#term-mapping)
- each key and value are patterns (dictionary like syntax)
- each pattern does not attempt to match the same key more than once
- subject must be an instance of [collections.abc.Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)

~~~python
match config:
    case {"route": route}:
        process_route(route)
    case {constants.DEFAULT_PORT: sub_config, **rest}:
        process_config(sub_config, rest)
~~~

---
# **Class Pattern**

- comparison is determined by an ```isinstance()``` call
<br>

~~~python
match point:
    case Point2D(x=x, y=y):
        print(f"point ({x}, {y})")
    case Point3D(x, y, z):  # requires __math_args__ (for positional argument matching)
        print(f"point ({x},{y},{z})")
~~~

---
# **```__match_args__```**

- shorthand to avoid specifying the attribute names in the class pattern
- ```__match_args__``` arg order could be different from ```__init__``` parameter order (Bad practise, useful for explicit cases).

~~~python
class Point3D:
    __match_args__ = ("x", "y")  # could also be a list

    def __init__(self, x, y, z):
        ...

match point:
    case Point2D(x=1, y=y):  # doesn't require __match_args__
        print(f"point ({x}, {y})")  # NameError: name x is not defined. 
    case Point3D(1 as x, y, z=z):  # not all arguments have to be specified by __match_args__
        print(f"point ({x},{y},{z})")
~~~

---
# **OR Pattern**

- Combines multiple patterns into one using |
- Alternatives are tried left->right

~~~python
match something:
    case 1 | x: # Error
        ...

    case 0 | 1 | 2:
        print("Small number")
    case [] | [_]:
        print("A short sequence")
    case str() | bytes():
        print("Something string-like")
    case _:
        print("Something else")
~~~

---
# **Guards**

- if expression (adding conditions to patterns)

~~~python
match input:
    case [x, y] if x == y:
        ...
~~~

---
### **Assignment expressions (walrus operator)**

- can avoid repetition / more efficent matches

~~~python
match get_shape():
    case Line(start := Point(x, y), end) if start == end:
        print(f"Zero length line at {x}, {y}")
~~~
<br>

### **As pattern**

- matches pattern(left-hand side) and binds a value to a name
- cleaner than using walrus operators

~~~python
match command.split():
    case ["go", ("north" | "south" | "east" | "west") as direction]:
        current_room = current_room.neighbor(direction)
~~~

---
# **Src / Read more**

- [overview](https://www.python.org/dev/peps/pep-0622/)
- [specifications](https://www.python.org/dev/peps/pep-0634/)
- [motivation and rationale](https://www.python.org/dev/peps/pep-0635/#as-patterns)
- [tutorial](https://www.python.org/dev/peps/pep-0636/)
- [precise semantics (behind the scenes)](https://www.python.org/dev/peps/pep-0653/)
- [feature overview (blog post)](https://benhoyt.com/writings/python-pattern-matching/)
