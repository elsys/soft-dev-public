---
theme: default
class: 
    - lead
    - invert
paginate: true
footer: '![width:40px](https://elsys-bg.org/web/images/logo.svg) ТУЕС - Разработка на софтуер - 2021/2022 - Владимир Алексиев '
---
# **Разработка на софтуер**
Лекция 04

## HTTP && Flask

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
# **Протокол**
- система от процедури и правила, по които се извършва даден процес
- http, ftp, tcp, etc.

---
# **Интернет**
- искаме да се свържем с друга машина по мрежата (машинит имат IP адреси)
- операционната система изпраща пакет насочен за адреса на другата машина
- той минава през рутера вкъщи и други подобни (hop-ове) и стига до адресата
- ако връзката е TCP (transfer control protocol) пакетите са доставени гарантирано
- повечето от това е скрито от вас

---
# **Мрежови сокети**
- комбинация от IP и Порт
- позволява на една машина да рабоят няколко софтуерни сървъра (на различни портове)

---
# **HTTP**
- hypertext transfer protocol
- client/server протокол
- първоначалната идея е за обмен на научни документи
- леко форматиран текс и некоя картинка понякога

---
# **HTTP**
- текстов
- без състояние
- клиента праща заявка, сървъра връща отговор
- порт 80 или 8080

---
# **HTTP заявка**
- headers
- body
или
- метаданни
- данни

---
# **HTTP headers**
- ключ: стойност
```
Host: code.tutsplus.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive
Cookie: PHPSESSID=r2t5uvjq435r4q7ib3vtdjq120
Pragma: no-cache
Cache-Control: no-cache
```
---
# **HTTP body**
- байтове 

---
# **HTTP методи/verbs**
- GET
- PUT
- POST
- DELETE
- PATCH
- HEAD
- OPTIONS

---
# **REST**
- `GET /users`
- `GET /users/1`
- `POST /users` `body: { id: 10, username: 'uname', age: 15 ... }`
- `PUT /users/1` `body: { username: 'bname', age: 15 ... }`
- `PATCH /users/1` `body: { age: 18 }`
- `DELETE /users/1`

---
# **virtualenv**
Виртуална Пайтън среда - като цяло библиотеките на няколко проекта не си пречат.

# **virtualenvwrapper**
Мениджър за виртуални среди

---
# **flask**

https://www.digitalocean.com/community/tutorials/getting-started-with-flask-a-python-microframework
