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

## Python - ООП

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
# ООП на идейно ниво

Парадигма, която ни позлволява лесно да моделираме проблеми от реалния (живия) живот като данни и алгоритми.

---
# ООП принципи
- Абстракция
- Енкапсулация
  - `public`, `private`, `protected`
- Модулярност 
- Наследяване и полиморфизъм

---
# ООП актьори
- класове
- обекти/инстанции
- член данни/променливи
- член функции/методи

---
# Python ООП
- всичко е обект
- обектите са отворени
- класовете са отворени

---
# Python ООП

```
class Vector:
    def __init__(self, x, y): # self is always first arg
        self.x = x # members are not declared explicitly
        self.y = y

spam = Vector(1.0, 1.0) # ClassName(arg1, arg2) creates an instance; self is _autowired_
print(spam.x) # instance.method() invokes a method
```

---

# `public`/`private`/`protected`

За разлика от други езици тук са пожелателни...

- по подразбиране всичко е публчно
- методи/атрибути започващи с `_` са защитени, т.е. би следвало да се ползват само от методи на класа и наследяващи го класове
- методи/атрибути започващи с `__` са частни, т.е. би следвало да се ползват само от методи на класа
- в някои много редки случаи може да се наложи тези ограничения да не се спазят

---


```
class Vector:
    def __init__(self, x, y, z):
        self.__private_init(x, y, z)
    
    def __private_init(self, x, y, z):
        self.x, self.y, self.z  = x, y, z
    
    def _coords(self):
        return (self.x, self.y, self.z)
    
    def length(self):
        return sum(_ ** 2 for _ in self._coords()) ** 0.5

```

---
# `unbound methods`

```
v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(4.0, 5.0, 6.0)
v3 = Vector(7.0, 8.0, 9.0)

print(Vector.length(v1))
print(Vector.length(v2))

print(list(map(Vector.length, [v1, v2, v3])))
print(list(map(lambda x: x.length(), [v1, v2, v3])))
```

---
# mutable vs immutable
```
class Vector:
    # ...
    
    def normalize(self):
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
    
    def normalized(self):
        return Vector(self.x / self.length(), self.y / self.length(),
        self.z / self.length())
```
---
# Сравняване на обекти
- можете да проверите дали два обекта са равни по стойност с `==`
- можете да проверите дали две имена сочат към един и същи обект с `is`
- можете да предефинирате равенството за обекти от даден клас с метода `__eq__`
- по подразбиране, `__eq__` е имплементирана с `is`

---
# Dunder методи
## Аритметични оператори
`__add__(self, other)` - `self + other`
`__sub__(self, other)` - `self - other`
`__mul__(self, other)` - `self * other`
`__truediv__(self, other)` - `self / other`
`__floordiv__(self, other)` - `self // other`

---
# Dunder методи
## Аритметични оператори
`__mod__(self, other)` - `self % other`
`__lshift__(self, other)` - `self << other`
`__rshift__(self, other)` - `self >> other`
`__and__(self, other)` - `self & other`
`__xor__(self, other)` - `self ^ other`
`__or__(self, other)` - `self | other`

---
# Dunder методи
## Преобразуване до стандартни типове
- `__int__(self)` - `int(обект)`
- `__float__(self)` - `float(обект)`
- `__complex__(self)` - `complex(обект)`
- `__bool__(self)` - `bool(обект)`

---
# Dunder методи
## `__call__`
```
class Stamp:
    def __init__(self, name):
        self.name = name
    
    def __call__(self, something):
        print("{0} was stamped by {1}".format(something, self.name))

stamp = Stamp("The government")
stamp("That thing there")
```
---
# `getattr`/`setattr`

достъпваме/променяме атрибути на обект динамично

```
v1 = Vector(1, 1, 1)
getattr(v1, 'y')

setattr(v1, 'z', 5)
getattr(v1, 'z')
```
---
# Статични методи/променливи

На идейно ниво - методи и данни, които не зависят от инстанция, а _жиевеят_ на ниво клас.

```
class GoatSimulator:
    goats = []

    @staticmethod # decorator - will talk about this later
    def register(name):
        GoatSimulator.goats.append(name)
        print(len(GoatSimulator.goats), " goats are registered now")
```
---
# Класови методи
Като статични, но получавате класа от който е извикан метода като първи аргумент

```
class Countable:
  _count = 0

  def __init__(self, data):
      self.data = data
      type(self).increase_count()

  @classmethod
  def increase_count(cls):
      cls._count += 1

  @classmethod
  def decrease_count(cls):
      cls._count -= 1
```
---
# `@property`/`property.setter`
```
class Goat:
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait
    
    @property
    def desc(self):
        return "{} the {} goat".format(self.name, self.trait)
    
    @desc.setter
    def desc(self, val):
        self.name = val
      

g = Goat("George", "Gutsy")
```

---
# Добавяне и изтриване на данни
```
class Person:
    def __init__(self, name):
        self.name = name

ivan = Person('Ivan')
ivan.name
ivan.age
ivan.age = 18
ivan.age
del ivan.age
ivan.age
```

---
# `pass`
Когато искаш, но нямаш желание... 
```
class Person:
    def __init__(self, name):
        self.name = name

    def age(self, age):
        pass
```
---
# Вектора като колекция
```
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]
    
    def __str__(self):
        return str((self.x, self.y, self.z))
    
    def __len__(self):
        return 3
    
    def __add__(self, other):
         return Vector(*map(sum, zip(self, other)))
```
---

# Можем и да присвояваме

```
class Vector:
    # …
    def __init__(self, x, y, z):
        self.x, self.y, self.z  = x, y, z
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            pass # тук можем да хвърлим изключение

v = Vector(1, 2, 3)
v[1] = 10
print(v.y) # 10
```
---
# Имплементационни детаили
Обектите в Пайтън са:
- речник, съдържащ атрибутите на обекта (атрибута `__dict__` на обекта)
- връзка към класа на обекта (атрибута `__class__` на обекта)

```
class Spam: pass

spam = Spam()
spam.foo = 1
spam.bar = 2
print(spam.__dict__)
print(spam.__class__)
print(spam.__class__ is Spam)
```
---
# Имплементационни детаили
Функциите и променливите дефинирани в тялото на класа са атрибути на класа.

```
class Spam:
    def foo(self):
        return 1

    bar = 42

print(Spam.foo)
print(Spam.bar)
```
---
# Имплементационни детаили
когато види `object.attr`прави следните неща:
- връща стойността на `object.__dict__['attr']`
- aко не намери, търси `object.__class__.attr`
  - ако не е функция се връща директно
  - ако е функция, се връща bound method
- aко го няма и там се вика `object.__getattr__('attr')`


---
# Наследяване
- в Python има наследяване
- всичко наследява от `object`

---
# Наследяване

```
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def name(self):
        return self.first_name + " " + self.last_name

class Star(Person):
    def greet_audience(self):
        print("Hello Sofia, I am {0}!".format(self.name()))

velizarkata = Star("Velizar", "Dimitrov")
velizarkata.greet_audience()
```
---
# Наследяване

```
class Person:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    
    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class Japanese(Person):
    def name(self):
        return "{0} {1}".format(self.last_name, self.first_name)

print(Person("Babatunde", "Adeniji").name())
print(Japanese("Yukihiro", "Matsumoto").name())
```

---
# Наследяване
```
class Person:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    
    def name(self)
        return "{0} {1}".format(self.first_name, self.last_name)

class Doctor(Person):
    def name(self):
        return "{0}, M.D.".format(Person.name(self))

print(Doctor("Gregory", "House").name())
```
---
# Наследяване
```
class Spam:
  def spam(self): return "spam"

class Eggs:
  def eggs(self): return "eggs"

class CheeseShop(Spam, Eggs):
  def food(self):
      return self.spam() + " and " + self.eggs()
```
---
# `Mixins`
- миксините са добра причина (една от малкото) за използване на множествено наследяване
- миксин класовете не се използват сами по себе си. Те са написани за да се наследяват.
- можете да гледате на Mixin като интерфейс (_?_) с имплементирани методи

---
# `Mixins`
- има два главни случая в които е добра идея да използвате Миксини
  - когато искате да "забъркате" множество атрибути и методи в един клас
  - когато искате клас който предлага само едно поведение и искате да го ползвате само като част от много други класове

- composition
  - https://www.infoworld.com/article/3409071/java-challenger-7-debugging-java-inheritance.html
---
# `Mixins`

```
class Screen: # ...
class RadioTransmitter: # ...
class GSMTransmitter(RadioTransmitter): # ...
class Input: # ...
class MultiTouchInput(Input): # ...
class ButtonInput(Input): # ...
class MassStorage: # ...
class ProcessingUnit: # ...

class Phone(ProcessingUnit, Screen, GSMTransmitter, 
            MultiTouchInput, ButtonInput, MassStorage): # ...

class Tablet(ProcessingUnit, Screen, RadioTransmitter, 
             MultiTouchInput, MassStorage): # ...
```
---
# `isinstance` и `issubclass`
```
print(isinstance(3, int)) # True
print(isinstance(4.5, int)) # False

print(issubclass(int, object)) # True
print(issubclass(float, int)) # False
```


