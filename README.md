## types

### basic types

* **numbers:**  [int](#), [float](), [complex]()
* **boolean:**  [bool](#)
* **none!:**  [NoneType](#), one constant has been defined for the only value it does take `None`

### strings 

* [str](#)


### collections

* `list`: [sample 1](./S02/collections/lists_in_python.py)
* `tuple`: [sample 1](./S02/collections/tuple_in_python.py)
* `dict`: [sample 1](./S02/collections/dict_python.py)
* `set`: [sample 1](./S03/collections-contd/python_sets.py)


## Operators

### unary 


| description | name of method | usage | example | 
|  ---   |  :---- | :---- | :---- |  :---- | 
| **negation** |  (`__neg__`)  |  `-self`  |  `-a` , `-1` |

| description | name of method | usage | example | 
|  ---   |  :---- | :---- | :---- |  :---- | 
| **not** |  (`__not__`)  |  `not self`  |  `not True`  |

### binary

| description | name of method | usage | example | 
|  ---   |  :---- | :---- | :---- |  :---- | 
| **add** |  (`__add__`)  |  `self + other`  |  `1 + 21` , `"hello" + "world"`     | 
| **sub** |  (`__sub__`)  |  `self - other`  |  `1 - 21` , `{1, 2, 3, 4} - {1, 2}`     | 
| **div** |  (`__div__`)  |  `self / other`  |  `1 / 21` , ` 102.1 / 2`     | 
| **mul** |  (`__mul__`)  |  `self * other`  |  `1 * 21` , ` "ATCGC" * 10`     | 
| **mod** |  (`__mod__`)  |  `self % other`  |  `100 % 2` , `"Hello %s" % ("Jack")`     | 
| **floordiv** |  (`__floordiv__`)  |  `self // other`  |  `1 // 21`     | 
| **pow** |  (`__pow__`)  |  `self ** other`  |  `2 ** 10`  | 


| description | name of method | usage | example | 
|  ---   |  :---- | :---- | :---- |  :---- | 
| **eq** |  (`__eq__`)  |  `self == other`  |  `1 == 21`, `(1, 2) == (1, 2)`  |
| **ne** |  (`__ne__`)  |  `self != other`  |  `1 != 21`  |
| **gt** |  (`__gt__`)  |  `self > other`  |  `1 > 21`  |
| **ge** |  (`__ge__`)  |  `self >= other`  |  `1 >= 21`  |
| **lt** |  (`__lt__`)  |  `self < other`  |  `100 < 2`  |
| **le** |  (`__le__`)  |  `self <= other`  |  `1 <= 21`  |


| description | name of method | usage | example | 
|  ---   |  :---- | :---- | :---- |  :---- | 
| **and** |  (`__and__`)  |  `self and other`  |  `True and True`  |
| **or** |  (`__or__`)  |  `self or other`  |  `True or False`  |
| **is** |    |  `self is other`  |  `a is b`  |
| **is not** |   |  `self is not other`  |  `a is not b`  |
| **in** |  (`__in__`)  |  `self in other`  |  `1 in [1, 2, 3, 4]`  |




## builtins 

### builtin functions 

* `print()`: 
* `type()`: 


### builtin types (cast type):

* `int()`,  `float()`,  `complex()`,  `str()`,   `bool()`,   `NoneType()`
* `list()`,  `tuple()`,  `dict()`,  `set()`
* `range()`


## Questions

* [BMI](./S04/conditional_statement/question.py)
* [leap year](./S04/conditional_statement/question2.py)
* [stars](./S05/loops/stars_question)
* [factorial (desc)](./S05/loops/factorial_2.py), [factorial (inc)](./S05/loops/factorial.py)