---
theme: default
class: 
    - lead
    - invert
paginate: true
footer: '![width:40px](https://elsys-bg.org/web/images/logo.svg) ТУЕС - Разработка на софтуер - 2021/2022 - Владимир Алексиев '
---
# **Разработка на софтуер**
Лекция 02

## Python
_до страница 40_

---
# **Уточнения**

- тази лекция се записва
  - съвременен български език
- _момчета_ === ученици

---
# **Уточнения**

- не съм Python експерт

---
# **Уточнения**

- тази лекция е базирана на материалите от Python курса във ФМИ от 2016
https://fmi.py-bg.net/


---
# 2,3,4...

- Python 2.7
- Python 3.6

---
# Къде го пишем

- `.py` файлове
- `$ python code.py`
- `$ python`

---
# Да опитаме

---
# `help()` <- документация on the go
```
>>> help(5)
>>> help(map)
>>> help(print)
```
---
# Синтаксис
- всеки ред код съдържа един израз
- никой ред код не съдържа `;`
- `#` бележи коментар
---
# Числа
- `int` - цели
- `float` - с точка
- без максимален размер
- `+`, `-`, `*`, `/`, `%`, `**`
---
# Низове
- текстови низове с произволна дължина
- единични или двойни кавички
- unicode навсякъде - енкодинг?
- поддържат `\n`, `\t` и пр.

---
# Низове
```       
>>> "hello".upper()
"HELLO"
>>> len("абвгдеж")
7
>>> "hello"[1]
"e"
>>> help(str)
```
---
# Енкодинг
Как представяме странни символи.

---

# Булеви стойности
- `True`
  - не `true`
- `False`
  - не `false`
---
# Нищо
- като `null`, ама `None`
- функция, която не връща, връща `None`
---
# Всяко нещо има тип
```
>>> type(5.5)
<class 'float'>
>>> type("слон")
<class 'str'>
>>> type(len)
<class 'builtin_function_or_method'>
```
---
# Обекти all the way
- всяка стойност е обект и има клас, включително функциите
- **всичко** в python е обект, включително функциите и **типовете**
- как да проверим типа?

---
# Променливи
- променлива == име + тип
- имената нямат тип
---
# Структури от данни/Data stuctures
- списък - `list`
- речник - `dict`
- tuple - `tuple`/_кортеж_
- множество - `set`
---
# Списъци
- масив
- mutable
- бързи за достъп, бавни за търсене
- запзват реда
- елементите са със смесен тип
---
# Списъци
```
>>> my_lsit = []
>>> my_list = list()
>>> my_list.append('slon')
>>> my_list.append(5)
>>> my_list.append(len)
>>> print(my_list[1])
5
>>> my_list[1] == 5
True
```
---
# Списъци?
```
>>> my_list = ['foo', 'bar', 'baz']
>>> my_list[3] = 'foobar'
```

---
# Списъци
- `len`
- `del`
- `in`

---
# Списъци
- `len(my_list)`
- `del my_list[index]`
- `in`

---
# Речник/`dict`
- хеш таблица, хеш мап, асоциативен масив
- реад не е гарантиран
- ключ <-> стойност

---
# Речник/`dict`
```
>>> marks = { 'Hris': 4, 'Zlati': 5 }
>>> marks['Niki'] = 3
>>> marks['Zlati']
>>> 'Niki' in marks
>>> marks.get('Vladi')
>>> marks.get('Vladi', 666)
```
---
# Tuple/кортеж/n-торка
- наредена двойка, тройка, н-торка
- immutable
- гарантиран ред
---
# Tuple/кортеж/n-торка
```
>>> point = (4, 9)
>>> p_x, p_y = point
```
---
# Множество/Set
- няма повторения
- без ред
- без пряк достъп
- проверка за принадлежност
- обхождане

---
# Множество/Set
```
>>> unique_numbers = {2, 3, 5, 6}
>>> unique_numbers
{2, 3, 5, 6}
>>> unique_numbers.add(5)
>>> unique_numbers
{2, 3, 5, 6}
>>> unique_numbers.remove(5)
>>> unique_numbers
{2, 3, 6}
>>> my_list = [5, 1, 6, 6, 2, 3, 5, 5]
>>> set(my_list)
{1, 2, 3, 5, 6}
```
---
# Mutable/Immutable
- immutable са числата, низовете, `tuple`-ите, `True`, `False`, `None` etc.
- mutable e всичко останало
---
# Mutable/Immutable
```
>>> a = 5
>>> a += 5 # the thing that changes is the variable, not the number 5

>>> l = [1, 2, 3]
>>> l.append(4) # the thing that changes is the array itself
```
---
# Блокове код и скоби
- всеки блок код (тяло на `if`, тяло на функция, и т.н.) се определя с индентацията му спрямо обгръщащия го блок.
- всеки блок код започва само след двуеточие в края на предишния ред.
- блокът свършва, когато се върнете към предишната индентация.
- 4 празни места = нов блок; **не 2, 3, ... n, не табулация**

---
# Контролни структури/оператори
- `if .. elif ..  else` 
- `while`
- `for`
- без скоби
---
# Контролни структури/оператори
- `and`
- `or`
- `not`
---
# Контролни структури/оператори
```
if a == 5:
  print("a is five")
elif a == 3 and not b == 2:
  print("a is three, but b is not two")
else:
  print("a is something else or b is two")
```
```
a = True
if a:
  print("a is True")

if not a:
  print("a is not True")
```
---
# Истина/Лъжа
Като лъжа се оценяват:
- `False`
- `None`
- `0` във всичките си форми
- `''` 
- празни колекции
- поведението на наши типове дефинириаме ние
---
# Истина/Лъжа
Като истина се оценяват:
- всичко останало
---
# `if`
```
my_list = [1, 2, 3, 4]

if 1 in my_list:
  print('1 is in my list')

if 5 not in my_list:
  print('5 is not in my list')
```
---
# `format`
- като `printf`, a `{}` в низа се попълват с аргументите.
- `{name}`, `{age}`,... могат да се именуват
- `{0}`, `{1}`, ... могат да се номерират
- `{:d}`, `{:f}`, ... могат да форматират аргументите
---
# `while`
```
while a > 5:
  a -= 1
  print("a is {}".format(a))
```
---
# `for`
Като `foreach` в други езици:
```
primes = [3, 5, 7, 11]
for e in primes:
  print(e ** 2) # 9 25 49 121

people = {'bob': 25, 'john': 22, 'mitt': 56}
for name, age in people.items():
  print("{} is {} years old".format(name, age))
```
---
# `for`
Като `for` в други езици:
```
for i in range(0, 20):
  print(i)

for i in range(0, 20, 3):
  print(i)

for i in range(20, 0, -1):
  print(i)

for i in range(20, 0, -3):
  print(i)
```
---
# `break/continue`
- работят като навсякъде
- работят върху най-вътрешния цикъл, ако има вложени
---
# `match/case`
```
match x:
  case 5:
    print("integer")
  case "Hello":
    print("string")
  case True:
    print("boolean")
  case default:
    print(f"x is {default}")
```
[Виж повече](match.md)

---
# Функции
Функциите в `python` са функции :)
- започват с `def`
- няма типове, на аргументите или резултата
- с `return` се връща резултат
- ако няма `return` връща `None`
---
# Функции
```
def multiply(a, b=2):
  return a * b

multiply(5)
multiply(5, 10)

def is_pythagorean(a=2, b=3, c=4):
  return a * a + b * b == c * c

is_pythagorean(b=5) # a = 2, c = 4
is_pythagorean(1, c=3) # a = 1, b = 3
```
---
# Терикатски функции
```
def calculate_volume_and_area(point_a, point_b, point_c): 
  volume = calculate_volume(point_a, point_b, point_c)
  area = calculate_area(point_a, point_b, point_c)
  return ________


________ = calculate_volume_and_area(...)
```
---
# Терикатски функции
```
def calculate_volume_and_area(point_a, point_b, point_c): 
  volume = calculate_volume(point_a, point_b, point_c)
  area = calculate_area(point_a, point_b, point_c)
  return (volume, area)


volume, area = calculate_volume_and_area(...)
```
---
# Терикатски функции

```
def varfunc(some_arg, *args, **kwargs):
  # ...

varfunc('hello', 1, 2, 3, name='Bob', age=12)
# some_arg == 'hello'
# args = (1, 2, 3)
# kwargs = {'name': 'Bob', 'age': 12}
```
---
# Терикатски функции
- функциите могат да приемат произволен брой аргументи
- позиционните аргументи (тези без име) отиват в `args`, което е `tuple` от агументи
- именуваните аргументи отиват в `kwargs`, което е `dict` от имена на аргументи и съответните им стойности
- имената `args` и `kwargs` не са специални, **но са наложена конвенция**; като `argc` и `argv`
---
# Функционално програмиране/Ламбда
- ако има време
- ще го говорим много :)



