# coding : utf-8

import os
import psutil

print("Это новая Прога - DAriec")

name = input("Ваше Имя: ")
print ("Привет", name, "!!!")

work = input("Хочешь ли Ты поработать? (Да/Нет)")


if work == "Да":
    print("        ")
    print("Что Ты хочешь сделать?")
    print("[1] - Подключится удаленно к рабочему ПК")
    print("[2] - Зайти в почтовый клиент")
    print("[3] - Вывести файлы в директории")
    print("[4] - Вывести информацию о системе")
    print("[5] - Сделать резервные файлы")

	
elif work == "Нет":
    print("        ")
    print("До свидания - ЛЕНТЯЙ!!")
    
else:
    print("        ")
    print("Неправильно ввели ответ! Введите повторно")

action = int(input(">>> "))

if action == 1:
    print("Вы успешно подключились к удаленному ПК")

elif action == 2:
    print("Вы успешно запустили почтовый клиент")

elif action == 3:
    print(os.listdir())

elif action == 4:
    print(sys.platform)
    print(polosa)

    print(sys.path)
    print(polosa)

    print("Имя ПК: ", os.environ['COMPUTERNAME'])
    print(polosa)


    print("Домен: ", os.environ['USERDOMAIN'])
    print(polosa)

    print("Логин: ", os.environ['USERNAME'])
    print(polosa)

    print("Операционная Система: ", os.environ['OS'])
    print(polosa)

    print("Архитектура Процессора: ", os.environ['PROCESSOR_ARCHITEW6432'], " - ",os.environ['PROCESSOR_ARCHITECTURE'])
    print(polosa)

    print("Путь: ", os.getcwd())
    print(polosa)

elif action == 5:
    print("Дублирование файлов в текущей директории")
    file_list = os.listdir()
    i = 0
    while i < len(file_list):
        newfile = file_list[i] + '.dupl'
        shutil.copy(file_list[i], newfile)

else:
    print("Вы неправильно выбрали действие. Введите повторно")


    
