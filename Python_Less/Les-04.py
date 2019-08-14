# coding : utf-8

import os
import psutil
import sys

polosa = "------------------"
print("Это новая Прога - DAriec")

#file_list = os.environ()
file_create = os.environ['USERNAME'] + '.bckp'
print(file_create)

compname = (os.environ['COMPUTERNAME'])

file = open(file_create, "w")
file.write(" Имя ПК: " + os.environ['COMPUTERNAME'] + '\n')
file.write(" Домен: " + os.environ['USERDOMAIN'] + '\n')
file.write(" Логин: " + os.environ['USERNAME'] + '\n')
file.write(" Операционная Система: " + os.environ['OS'] + '\n')
file.write(" Архитектура Процессора: " + os.environ['PROCESSOR_ARCHITEW6432'] +" - " + os.environ['PROCESSOR_ARCHITECTURE'] + '\n')
file.close()
