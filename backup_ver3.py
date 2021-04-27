import os
import time

#1. Файлы и каталоги, которые необходимо скопирповать, собираются в список.
source = ['H:\\Python']
# 2. Резервные копии должны храниться в основном каталоге резерва
target_dir = 'H:\\Backup' #Поставьте ваш путь

# 3. Файлы помещаются в zip архив
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir+os.sep+time.strftime("%Y.%m.%d")
#Текущее время служит именем Zip-архива

now = time.strftime('%H"."%M"."%S')

#Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # Проверяем, введйн ли комментарий
	target = today + os.sep + now +'.zip'
else:
	target = today + os.sep + now + '_' + \
	 comment.replace(' ', '_') + '.zip'



#Создаём каталог, если его еще нет

if not os.path.exists(today):
	os.mkdir(today) #Создание каталога
	print('Каталог успешно создан',today)



# 5. Используем коменду "zip" для помещения файлов в архив

zip_command = "RAR  a -r {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии

if os.system(zip_command)  == 0:
	print('Резервныя копия успешно создана в',target)

else:
	print("Создание копии не удалось")
