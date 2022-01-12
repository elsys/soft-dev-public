---
theme: default
class: 
    - lead
    - invert
paginate: true
footer: '![width:40px](https://elsys-bg.org/web/images/logo.svg) ТУЕС - Разработка на софтуер - 2021/2022'
---
# **Разработка на софтуер**

Процес по разработка на софтуер 

Лекция 04 - Спецификация

---
# **Защо ни е нужна спецификация (1)**


- Agile няма безкрайна документация, но все пак има спецификация 

![width:750px](https://assets.amuniversal.com/d2f593406cc901301d50001dd8b71c47)

---
# **Защо ни е нужна спецификация (2)**

- Всички хора от екипа работят с еднакви разбирания за функционалностите
- По-добра естимация на работата
- По-добро разбиране на ползата от продукта и как клиентите ще работят с него
- Приоритизация и планиране на проекта
- Различни екипи (или хора) могат да работят в паралел
- По-лесно добавяне на нови хора в екипа
 
---
# Стъпки за създаване на спецификация (1)

- Участници от екипа:  Бизнес екип, Product Owner, Бизнес анализатор

- Краен продукт на работата на екипа:
  - Приоритизиран продуктов беклог
  - Одобрение от бизнес екипа
  - Продуктов roadmap
  - Идентифицирани специфични знания нужни на екипа
  
---
# Стъпки за създаване на спецификация (2)

- 1. Идентифициране на проблем, който продуктът решава
- 2. Интервюта с клиенти и бизнес екипа
- 3. Създаване на персона за всеки потребител
- 4. Разбиране и предлагане на решения за трудностите на всеки потребител
- 5. Обсъждане на идеи и приоритизация
- 6. Създаване на обхват на проекта (първа версия – Minimum Viable Product)
- 7. Създаване на продуктовия беклог
- 8. Детайлно описание на функционалностите

---
# Design Thinking

![width:800px](https://suebehaviouraldesign.com/wp-content/uploads/2018/12/Design-Thinking-Ideo.jpg)

---
# Дефиниция на персони

- Целта е да разберем как мисли и да се поставим на мястото на потребителя
- Пресъздаваме ежедневието му и търсим решения за проблемите, които среща

![width:700px](https://miro.medium.com/max/1200/1*I1ffOWdPWQva3dCMQE-TAQ.png)

---
# Структура на беклога (1)

![width:800px](https://basquang.com/wp-content/uploads/2021/03/031921_0836_AgilePlanni3.png)

---
# Структура на беклога (2)

Различни елементи според нивото на детайл на всяка стъпка:

- Theme – големи инициативи част от визията на компанията (6-12+ месеца)
- Epic – доставя цяла фунционалност решаваща проблем на клиента (3-6 месеца)
- Feature – атомарна функционалност, доставяща конкретна част от epic (1-2 месеца)
- User story – конкретни изисквания от перспективата на потребителя (1 спринт)
- Task – конкретни технически задачи за имплементация (часове до 2-3 дни)

---
# Epic (1)

Описваме групата хора, за които се отнася, предложеното решение, как се различава от сегашното и защо е по-добре (т.е. каква е добавената стойност)

For <customers>
who <do something>
the <solution>
is a <something – the “how”>
that <provides this value>
unlike <competitor, current solution, missing solution>
our solution <does something better – the “why”>

---
# Epic (2)

For the parents
who want to know their children's grades
the online grading system
is a way for them to access these grades
that on demand provides the latest data
unlike paper school books
our solution is always accessible, more accurate and reliable

---
# Epic (3)

For the students
who want to play Belote
the GUI for our Belote solution
is a way to visualize the cards being played
that makes the game more user friendly and interactive
unlike the console Belote version
our solution is much more fun, has better user experience and improves adoption

---
# User Story (1)

Какво пишем в едно user story:
- За какъв потребител (персона) се отнася
- Какво точно прави този потребител
- Какъв ефект постига
- Definition of “done” – какво е нужно, за да се приеме story-то за готово
- Описание стъпка по стъпка

“As a [persona], I [want to], [so that].”

---
# User Story (2)

As a student, I want to implement a version of Belote for 3 players, so that when there are not enough players we can still play.

As a frequent flyer, I want to rebook a past trip, so that I save time when I book trips I take often.

As a student I want to integrate Google’s voice recognition API, so that when my number gets called it recognizes it.

As a DevOps engineer, I want to create a backup procedure for our databases, so that we don’t lose data in the event of a failure.

---
# MVP – Minimum Viable Product (1)

Проблем: Всички искат от самото начало много функционалности – всичко, което е в дългосрочната им визия и желания за развитие на продукта.

Реалност: Това би отнело много време, може да се окаже грешно и ненужно, няма достатъчно бюджет за него и може да пропусне пазарната си реализация.

---
# MVP – Minimum Viable Product (2)

Решение:
- Дефинираме минимален продукт, който клиент може да използва (MVP)
-  Той няма да съдържа всички супер готини неща, които искаме да има
- Валидираме пазара и искаме обртна връзка от потребителите си
- Дефинираме следващи итерации за надграждане на продукта базирани на тази обратна връзка

---
# MVP – Minimum Viable Product (2)
![width:800px](https://catalystsguild.com/wp-content/uploads/2019/02/donut2.jpg)

---
# Start with a cupcake
![width:700px](https://blog.intercomassets.com/blog/wp-content/uploads/2014/07/Acupcake740.png)
- https://www.intercom.com/blog/start-with-a-cupcake/
