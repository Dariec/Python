# coding: utf-8
import math

print("        ")
print("РадиоКалькулятор 1.0v")
print("Автор: Дмитрий Павлухин")


dBm = 0
work = 0
answer = 'Y'

while answer != 'Q':
    print("        ")
    print('Какую команду мне выполнить?')
    print('1 - Перевод из dBm в W')
    print('2 - Перевод из W в dBm')
    print('Q - Выйти из программы.')

    work = int(input(">>> "))

    if work == 1:
        print("        ")
        dBm = int(input("Введите dBm >>>  "))
        a = dBm / 10
        b = 10 ** a
        c = b / 1000
        print("Введено: ", dBm, "dBm")
        print("МиллиВатт: ", "%.3f" % b, "mW")
        print("Ватт: ", "%.4f" % c, "W")



    if work == 2:
        print("        ")
        W = int(input("Введите W >>>  "))
        print("Введено: ", W, "W")
        print("Децибел-Вт: ", "Тут потом будет еще инфа")
