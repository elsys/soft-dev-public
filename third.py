#Даден е Python списък от елементи - низове, числа, списъци (вкл. като този), наредени н-торки. 
#Да се напише функция `replace` с 3 аргумента - `list`, `find`, `replace`,  където list e писък от типа по-горе, 
#a find и replace са низове. Функцията връща нова версия на `list` в която всяко срещане на `find` e заменено  с `replace`.
#task 3

def replace(list, find, replace1):
	new_list = []
	ch = 0
	for i in list:
		if i == find:
			list[ch] = replace1
		if type(i) != int:
			if len(i) > 1:
				new_list = list[ch]
				replace(new_list,find,replace1)
		ch = ch + 1
	return list

list = ['a',1,[['a','b'],1],([1,3,'a'],'b')]
res = replace(list,'a','c')
print(res) # => ['c',1,[['c','b'],1],([1,3,'c'],'b')]
