#'ab' - сокращение от "a"ddress 'b'ook

ab = {'Dimon'      : 'hoster100@mial.ru',
      'Diana'      : 'Myska1999@gmail.com',
      'Matsumoto'  : 'matz@ruby-lang.org',
      'Spammer'    : 'Spammer@hotmail.com'
      }

print("адрес Dimon'a:", ab['Dimon'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, adress in ab.items():
	print('Контакт {0} с адресом {1}'.format(name, adress))

# добавление пары ключ-значение
ab['Guido'] ='guido@python.org'


if "Guido" in ab:
	print('\nАдрес Guido:', ab["Guido"])

help(dict)