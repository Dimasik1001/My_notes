print('простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!
del shoplist[0] # Я сделал первую покупку, поэтому удаляю ее из списка

print('shoplist:',shoplist)
print('mylist:' ,mylist)
#Оратите внимание, что shoplist и mylist выводят один и тот же список
#без пункта 'яблоко',потверждая тем самым, что они указывают на один объект

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию, при помощи полной вырезки
del mylist[0] # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist',mylist)
#Обратите внимание , что теперь списки разные