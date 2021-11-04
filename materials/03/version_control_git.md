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

Лекция 01 - Version control

---
# **Какво е version control система**

- Система, която проследява и записва промените по даден файл или набор от файлове
- Примери за version control системи
  - Centralized Version Control: CVS, Subversion
  - Distributed Version Control: Git, Mercurial, Bazaar
 
---
# Centralized vs. Distributed VCS

![width:650px](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190820174942/CVCS-vs-DVCS.png)

- Дистрибутираните системи позволяват на множество хора да работят по един проект без да поддържат връзка към обща мрежа

---
# Git

- Git e безплатна open source дистрибутирана система, подходяща както за малки, така и за големи проекти и екипи

- В момента Git е практически без аналог и най-широко използваната система при стартиране на нови проекти

- Всяка локална Git директория съдържа пълно копие на repository-то с пълна история

- Няма централизиран сървър и не е необходима постоянна връзка между работещите по проекта

---
# Състояния в Git

- Трите основни състояния на Git са:

![width:550px](https://image.slidesharecdn.com/git-intro-091215075529-phpapp01/95/git-and-github-13-728.jpg?cb=1260938801)

---
# Състояния в Git

- Git directory: съдържа мета данни и базата данни (обекти) на проекта при клониране

- Working directory: съдържа единично копие на проекта на локалния компютър, с което може да работите

- Staging area: обикновено локално създаден файл, който пази информация за промените, които ще влязат със следващия commit

---
# Състояния на файлове

- Всеки файл може да бъде в състояние Tracked или Untracked

- Tracked файловете могат да бъдат Unmodified, Modified или Staged

![width:550px](https://confluence.lsstcorp.org/download/attachments/4752122/gitFileStatus.png?version=1&modificationDate=1395067714000&api=v2)

---
# Проверка на статус

- Command: ***git status***
  - Tracked: файлове, които вече съществуват в проекта
  - Untracked: Файлове, които не са част от проекта (нови)
  
- Command: ***git add filename***  
  - Команда за промяна на статуса на trackable

---
# Създаване на ново repository

- Съществуващ проект
  - git clone URL
  
- Нов проект
  - git init
  - git add &ast;.&ast;
  - git commit -m "Initial commit"
  - git push origin master

---
# Разлики във файлове

- Command: ***git diff***
  - Показва разликите между staged и unstaged файлове

- Command: ***git diff -cached***
  - Показва разликата между staged и последното състояние в repository-то (commited)

---
# Commiting на промени

- Command: ***git commit***
  - Най-лесният начин да се направи commit

- Command: ***git commit -m "Comment"***
  - Commit задно с коментар (препоръчително)

- Command: ***git commit -а -m "Comment"***
  - Commit задно с коментар и пропускане на staging area-та
  
---
# Премахване на файлове

- Command: ***git rm filename***
  - Премахване на файл

- Command: ***git rm --cached filename***
  - Премахване на файл от staging area-та

- Command: ***git mv file_from file_to***
  - Преименуване на файл
---
# История на commits

- Command: ***git log***
  - Преглеждане на commit историята

- Command: ***git log p***
  - Преглеждане на разликите във всеки commit

---
# Промяна на commit

- Command: ***git commit -amend***
  - Промяна на последния commit
  
- Примери
  - git commit -m "Comment" // Създаване на commit
  - git add filename // Забравен файл към commit
  - git commit -amend // Файлът се добавя без създаване на нов commit

---
# Работа с отдалечено repository

- Command: ***git push origin branch_name***
  - Публикуване на нашия код в отдалеченото repository 

- Command: ***git pull***
  - Изтегляне на нови промени от отдалеченото repository

- Command: ***git fetch***
  - Изтегляне на нови бранчове в локалната директория
  
---
# Работа с бранчове

- Command: ***git checkout -b branch_name***
  - Създаване на бранч в локалното repository

- Command: ***git branch -d branch_name***
  - Изтриване на бранч от локалното repository
  
![width:400px](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)

---
# Merge-ване на бранчове

- Merge-ване на съществуващи паралелни промени, запазвайки историята промените във всеки от тях

- Пример:
  - git checkout dev  // Сменяме към development бранча
  - git pull // Изтегляме последните промени от repository-то
  - git merge story_1145 //  Merge-ваме промените от наш локален бранч в development
  - git push origin dev // Качваме новия development бранч в отдалеченото repository
  
---
# Branching стратегия

![width:400px](http://nvie.com/img/git-model@2x.png)

---

# Rebasing 

- Rebasing е преместването на един (или повече) commit към нова базов commit

- Command: ***git rebase branch_name***

![width:400px](https://wac-cdn.atlassian.com/dam/jcr:4e576671-1b7f-43db-afb5-cf8db8df8e4a/01%20What%20is%20git%20rebase.svg?cdnVersion=1834)

---
# Допълнителна информация

- https://guides.github.com/introduction/git-handbook/

- https://www.atlassian.com/git/tutorials
