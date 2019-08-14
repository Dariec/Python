# coding : utf-8

import os
import psutil
import sys

polosa = "------------------"
print("Это новая Прога - DAriec")

name = input("Ваше Имя: ")
print ("Привет", name, "!!!")


answer = ""
while answer != 'q':
    answer = input("Хочешь ли Ты поработать? (Y/N/q)")
    if answer == "Y":
        print("        ")
        print("Что Ты хочешь сделать?")
        print("[1] - Подключится удаленно к рабочему ПК")
        print("[2] - Зайти в почтовый клиент")
        print("[3] - Вывести файлы в директории")
        print("[4] - Вывести информацию о системе")
        
    elif answer == "N":
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

    else:
        print("Вы неправильно выбрали действие. Введите повторно")


