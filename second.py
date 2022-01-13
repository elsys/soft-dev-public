#Дадена е стълба с N >= 2 стъпала. Стоим в началото на стълбата и можем да качим 1 или 2 стъпала наведнъж. 
#Да се напише функция, `num_ways` която по подадено N връща броя на начини по които можем да изкачим
#стълбата - т.е. да стъпим на N-тото стъпало.
#task 2

def num_ways(steps):
	if steps <= 2:
		return steps
	else:
		return num_ways(steps-1) + num_ways(steps-2)

steps = 3
print(num_ways(steps))


