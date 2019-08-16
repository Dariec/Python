# coding : utf-8

import os
import psutil
import sys
import random

def ping():
        rand = random.randint(40, 57)
        num = num + 1
        print("Ответ от ", answer, " число байт=32 время=", rand, "мс TTL=55")

        if num == endnum:
            print("Статистика Ping для ", answer)
            print("Пакетов: отправлено = ", num, ", получено =", num, ", потеряно = ", 0)


polosa = "------------------"
print("Это новая Прога - DAriec")




print("Введите IP адрес что бы выполнить PING")
answer = input("Для примера >>  192.168.1.1 >>>   ")

num = 0
endnum = int(input("Введите количество пакетов >>>   "))

print("Обмен пакетами с ", answer, " с 32 байтами данных:")

while num != endnum:
        ping()
