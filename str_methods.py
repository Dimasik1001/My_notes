name='swaroop' # Это объект строки

if name.startswith('swa'):
	print('Да, строка начинается на "swa"')

if 'a' in name:
	print('Да, строка содержит "а"')

if name.find('war') != -1:
	print('да, она содержит строку "war"')

delimiter = '|(.)(.)|'#Это губка боб
mylist = ['Бразилия', 'Россия','Индия', 'Китай']
print(delimiter.join(mylist))