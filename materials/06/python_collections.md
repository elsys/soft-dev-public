---
theme: default
class: 
    - lead
    - invert
paginate: true
footer: '![width:40px](https://elsys-bg.org/web/images/logo.svg) ТУЕС - Разработка на софтуер - 2021/2022 - Владимир Алексиев '
---
# **Разработка на софтуер**
Лекция 03

## Python - колекции

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
# **Подготовка за дистанционно обучение**
Шансовете са в обозримо бъдеще да сме онлайн :/

- ако не използвате камера не се брои - отсъствие
- ако не използвате микрофон не се брои - без шанс за бонбони
- Google Meet може да манипулира фона

---
# **Стил**
![width:900px](https://c.tenor.com/dKsgOdO926AAAAAC/harry-potter-you-gotta-admit.gif)

---
# **Стил**
Styleguide
- PEP8
- конфигурирайте едиторите си
- повечето езици имат такъв - намерете го и го използвайте
- линтери/style checker-и

---
# **Стил**
- индентация с 4 интервала
- 79 символа
- `snake_case` - променливи, параметри, функции и методи
- `SCREAMING_SNAKE_CASE` - за _константи_
- `_private` - за частни методи/променливи
- `__real_private` ---> `ClassName_real_private` - имомачкане
- `class_`, `range_` - подчертавка след името за запазени думи 
---
# **Не баш стил**
## `__new__`, `__init__`, `__add__`, `__bool__`, `__iter__` 
магически/дъндер методи
![image](https://c.tenor.com/wn2_Qq6flogAAAAC/magical-magic.gif)


---
# **Колекции**
- `list`
- `typle`
- `set`
- `dict`

---
# **Интерфейс**
- _iterable_ - итеруеми
  - `__iter__`, 
    - `ClassIterator`, 
      - `__next__`
- итеруем обект може да бъде обходен поне веднъж (деструктивно обхождане)
- някои могат да бъдат обходени многократно

---
# Списъци

---
# Списъци
```
blue_things = ['небето', 'морето', 'очите на Апостола']
for thing in blue_things:
  print("- Какво е синьо?")
  print(
    "- {}{}!".format(
      thing[0].upper(), 
      thing[1:],
    )
  )
```
---
# _Като говорим за низове_
https://waymoot.org/home/python_string/

---
# Списъци - индекси

```
blue_things = ['небето', 'морето', 'очите на Апостола']
blue_things[2] == blue_things[-1]
blue_things[1] == blue_things[-2]
blue_things[0] == blue_things[-3]
```

---
# Списъци - индекси
## парчета
```
cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']

# cute_animals[start:stop]

cute_animals[1:3]  # ['raccoon', 'panda'] <- NO STOP
cute_animals[-1]  # 'marmot'
cute_animals[1:-1]  # ['raccoon', 'panda', 'red panda'] <- NO STOP
```

---
# Списъци - индекси
## издължени парчета
```
cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']

# cute_animals[start:stop:step]

cute_animals[::-1]  # ['marmot', 'red panda', 'panda', 'raccoon', 'cat']
cute_animals[-1:0:-1]  # ['marmot', 'red panda', 'panda', 'raccoon']
cute_animals[-1:0:-2]  # ['marmot', 'panda']
```
---
# Списъци
## Списъците съдържат _указатели_ към елементи

```
# unpacking
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea' 

things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

things_i_like[0] == things_i_like[1] # True
things_i_like[0] is things_i_like[1] # True
```

---
# Списъци

```
cheeses = ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto']
cheeses.append(cheeses)

cheeses[-1] is cheeses # True

print(cheeses) # ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto', [...]]
print(cheeses[-1]) # ?
```

---
# Списъци - методи
- `.index(element)` - индекса на първото срещане на element в списъка или гърми с ValueError
- `.count(element)` - броят срещания на element в списъка
- `.append(element)` -добавя element в края на списъка
- `.extend(elements)` - добавя елементите на elements в списъка (като + ама по-бързо)
- `.sort()` - сортира
- и т.н.

---
# Излъгах ви...
## `range` не е генератор, а итеруем обект
#### _но е много подобно на генераторите за които ще си говорим друг път_

---
# `tuple`

---
# `tuple`
- n-торка, кортеж
- като списък, но с постоянен ред, 
  - завинаги

---
# `tuple`
```
teams = ('Levski', 'Litex', 'Botev Plovdiv')
teams[2] # Botev Plovdiv
teams[1] # Litex
teams[0] # Levski

teams[1] = 'CSKA'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Litex is not CSKA
```

---
# `tuple`
```
teams[1] = 'CSKA'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

---
# `tuple`

## съдържанието може да се променя
```
change_me = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
change_me[1][1] = 0
change_me[2][0] = 'c'

print(change_me) # ([1, 2, 3], [4, 0, 6], ['c', 8, 9])
```

---
# `tuple`
## Mожем и без скоби

```
teams = 'Levski', 'Litex', 'Botev Plovdiv'
teams = 'Levski', 

teams = ('Levski')
```

---
# Фончо Териката - `tuple` едишан

```
(a, b) = (1, 2)
(a, b) = 1, 2
a, b = (1, 2)
a, b = 1, 2
point = (3, 5)
x, y = point
first, *rest, last = (1, 2, 3, 4, 5, 6)
```

---
# Стек, Опашка
- стек
- опашка

---
# Множества
- като списък, но без ред и повторение
```
fav_nums = set()
fav_nums.add(1914)
fav_nums.add(7)
fav_nums.add(2)
fav_nums.add(8)
fav_nums.add(0)
print(fav_nums)
```

---
# Множества

```
for num in fav_nums:
  print(num)

7 in fav_nums

fav_nums = { 1914, 7, 2, 8, 0 }

emoty_set = {}
```

---
# Множества - операции

```
{1, 2, 3} | {2, 3, 4}
{1, 2, 3} & {2, 3, 4}
{1, 2, 3} - {2, 3, 4}
{1, 2, 3} ^ {2, 3, 4}
{1, 2, 3} < {2, 3, 4}
{2, 3} < {2, 3, 4
{2, 3} == {2.0, 3}
{1, 2}.isdisjoint({3, 4})
```

---
# Речник

---
# Речник
- ключ => стойност
- `{}` е празен речник
```
countries = dict(france="Paris", italy="Rome")

numbers = dict([('One', 'I'), ('Two', 'II')])

with_default = dict.fromkeys([1, 2, 3], 'Unknown')
```

---
# Речник
```
artist_names = {
  'Eddie': 'Vedder',
  'Maynard': 'Keenan',
  'Matthew': 'Bellamy',
  'James': 'LaBrie',
}
print(artist_names)
```

---
# Речник

```
artist_names['Devin'] = 'Townsend'
print(artist_names)
```

---
# Речници и хеш функции
- f: обект -> число
- еднакви обекти => еднакъв хеш
- възможно е различни обекти да имат еднакъв хеш
- ключовете трябва да са сравними с `==` по смислен начин

---
# Функционална парадигма
- `map(function, iterable)` създава колекция от резултатите от прилагането на function върху всеки елемент от iterable
- `filter(function, iterable)` създава колекция само с елементите, за които function върне True
- `reduce(function, iterable)` вика function с елементите на колекцията, докато сведе всичко до една стойност
- `all(iterable)` всички елементи се оценяват на истина
- `any(iterable)` поне един от елементите се оценява на истина

---
# Функционална парадигма
- функция, която проверява дали всички числа в масив са четни на 1 линия

---
# List comprehensions
## [израз for променлива in итеруемо (if условие)]

- [ x * x for x in range(0, 10) ]
- [ x * x for x in range(0, 10) if x % 2 ]
- [ (x, y) for x in [1,2,3] for y in [3,1,4] if x != y ]

---
# Generator expression
## ( израз for променлива in итеруемо (if условие) )
- lazy valuation
- ( x**2 for x in range(1,10) )

---
# Set comprehensions
## { израз for променлива in итеруемо (if условие) }
- { x**2 for x in range(1,10) }

---
# Dict comprehensions
- `{ i: chr(65+i) for i in range(10) }`

---
# `collections`
- `from collections import ....`
- https://docs.python.org/3/library/collections.html
