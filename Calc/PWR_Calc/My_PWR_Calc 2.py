# coding: utf-8
import math

print("        ")
print("###############################")
print("Электронный коллега 1.3v ;-)")
print("Автор: Дмитрий Павлухин")
print("###############################")


V = 0
work = 0
answer = 'Y'


while answer != 'Q' or 'q' or 'Й' or 'Й':
    print("        ")
    print('Какую команду мне выполнить?')
    print('1 - Расчет - Время работы от АКБ')
    print('2 - Расчет - Время заряда АКБ')
    print("        ")
    print('Q - Выйти из программы.')

    work = int(input(">>> "))

    if work == 1:
        print("        ")
        Ah = float(input("Введите Ah >>>  "))
        V = float(input("Введите V >>>  "))
        W = float(input("Введите нагрузку W >>>  "))
        H = 60
        A = W / V
        a = A * H
        b = Ah / a
        c = H * b
        d = c / 24
        print("###############################")
        print("Введено: ", Ah, "Ah")
        print("Введено: ", V, "V")
        print("Введено: ", W, "W")
        print("%.1f" % c, "Hour")
        print("%.1f" % d, "Day")
        print("###############################")

    if work == 2:
        print("        ")
        Ah = float(input("Введите Ah >>>  "))
        V = float(input("Введите V >>>  "))
        A = float(input("Введите силу тока A >>>  "))
        H = 60
        a = Ah / A
        b = a * 1.4
        c = b / 24
        print("###############################")
        print("Введено: ", Ah, "Ah")
        print("Тепловые потери - 1.4")
        print('Зарядка данного АКБ будет занимать: ', "%.1f" % b, "Часов")
        print("###############################")



