class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('привет! Меня зовут', self.name)


p=Person('Dimon')
p.say_hi()

# Предыдущие 2 строки можно
# Person("Dimon").say_hi()
