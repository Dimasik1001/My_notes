

import sys 

print('Аргументы комендной строки:')

for i in sys.argv:
	print(i)


print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

import os
print(os.getcwd())
