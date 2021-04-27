

def printMax(x,y):
	'''Выходит максимальное из двух чисел.

	Оба значения должны быть целыми числами.'''
	x=int(x) # коныертируем в целые, если возможно
	y=int(y)

	if x>y:
		print(x,"наибольшее")
	else:
		print(y,'наибольшее')
printMax(3,5)

print(printMax.__doc__)
help(printMax)#хз зачем это нужно