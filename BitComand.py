  



while  True:
	a=int(input("Введите Первое число:"))

	b=int(input("Введите Второе число:"))


	print("Первое число: " + bin(a)) 
	print("Второе число: " + bin(b)) 
	print("Операция & : " + bin(a&b)+'(Изменяет 1 на 0)') 
	print("Операция | : " + bin(a|b)+'(Изменяет 0 на 1)')
	print("Операция ^ : " + bin(a^b)+'(Изменят 0 на 1,только если есть 0)')
	print("Операция ~ : " + " Для первого числа: "+bin(~a)+" Для второго числа: "+bin(~b)+'(Изменяет 0 на 1 и наоборот)')
	print("Операция << : " + " Для первого числа: "+bin(a<<2)+" Для второго числа: "+bin(b<<2)+'(сдвигает справа на лево на заданное количество бит)')
	print("Операция >> : " + " Для первого числа: "+bin(a>>2)+" Для второго числа: "+bin(b>>2)+'(сдвигает слева на право на заданное количество бит)')