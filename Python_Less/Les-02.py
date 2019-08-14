# coding : utf-8

import os
import psutil
import sys

polosa = "------------------"
print("Это новая Прога - DAriec")
#help(psutil)

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

