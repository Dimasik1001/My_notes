

number=23
running=True
while running:
	guess=int(input('Введите целое число:'))

	if guess==number:
		print('Поздравляю вы угадали.')
		running=False #Это останавливает цикл while
	elif guess < number:
		print('Нет, загаданное число немного больше этого.')
	else :
		print('Нет, загаданное число немного меньше этого.')
else:
	print("цикл while закончен.")
	# Здесь можете выполнять все что вам еще нужно

print("Завершение.")

