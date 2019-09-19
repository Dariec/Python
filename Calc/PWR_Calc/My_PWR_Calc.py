# coding: utf-8
import math

print("        ")
print("###############################")
print("Электронный коллега 1.0v")
print("Автор: Дмитрий Павлухин")
print("###############################")


V = 0
work = 0
answer = 'Y'


def cable_mm(mm):
    print("###############################")
    print("Для данной нагрузки подходит кабель с сечением жилы - ", mm, "мм")
    print("###############################")

while answer != 'Q':
    print("        ")
    print('Какую команду мне выполнить?')
    print('1 - Перевод из V в mV')
    print('2 - Перевод из mV в V')
    print('3 - Перевод из A в mA')
    print('4 - Перевод из mA в A')
    print('5 - Посчитать Мощность (A & V)')
    print('6 - Посчитать сечение жилы')
    print('Q - Выйти из программы.')

    work = int(input(">>> "))

    if work == 1:
        print("        ")
        V = float(input("Введите V >>>  "))
        a = V * 1000
        print("###############################")
        print("Введено: ", V, "V")
        print("МиллиВольт: ", "%.1f" % a, "mV")
        print("###############################")

    if work == 2:
        print("        ")
        V = float(input("Введите mV >>>  "))
        a = V / 1000
        print("###############################")
        print("Введено: ", V, "mV")
        print("МиллиВольт: ", "%.2f" % a, "V")
        print("###############################")

    if work == 3:
       print("        ")
       A = float(input("Введите A >>>  "))
       a = A * 1000
       print("###############################")
       print("Введено: ", A, "A")
       print("Ампер: ", "%.2f" % a, "mA")
       print("###############################")

    if work == 4:
        print("        ")
        mA = float(input("Введите mA >>>  "))
        b = mA / 1000
        print("###############################")
        print("Введено: ", mA, "mA")
        print("Ампер: ", "%.3f" % b, "A")
        print("###############################")

    if work == 5:
        print("        ")
        A = float(input("Введите A >>>  "))
        V = float(input("Введите V >>>  "))
        W = A * V
        kW = W / 1000
        print("###############################")
        print("Введено: ", V, "V", " - ", A, "A")
        print("Ватт: ", "%.1f" % W, "W")
        print("КилоВатт: ", "%.2f" % kW, "kW")
        print("###############################")

    if work == 6:
        print("        ")
        material = input("Какой материал кабеля? (C - медь; A - Алюминий >>>  ")
        lendth_cable = float(input("Введите длину кабеля (1-1000) >>>  "))
        Work_V = float(input("Введите рабочее напряжение  (1.5-5000 В) >>>  "))
        Work_W = float(input("Введите рабочую мощность  (1-10000 Вт) >>>  "))

        if material == "C":
            A = Work_W / Work_V
            if A < 19:
                mm = 1.5
                cable_mm(mm)
            if A > 19 and A <= 27:
                mm = 2.5
                cable_mm(mm)
            if A > 28 and A <= 38:
                mm = 4
                cable_mm(mm)
            if A > 38 and A <= 46:
                mm = 6
                cable_mm(mm)
            if A > 46 and A <= 70:
                mm = 10
                cable_mm(mm)
            if A > 70 and A <= 80:
                mm = 16
                cable_mm(mm)
            if A > 80 and A <= 115:
                mm = 25
                cable_mm(mm)
            if A > 115 and A <= 135:
                mm = 35
                cable_mm(mm)
            if A > 135 and A <= 175:
                mm = 50
                cable_mm(mm)
            if A > 175 and A <= 215:
                mm = 70
                cable_mm(mm)
            if A > 215 and A <= 265:
                mm = 95
                cable_mm(mm)
            if A > 265 and A <= 300:
                mm = 120
                cable_mm(mm)
            if A > 300:
                print("############################################################################################################################")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Значение #Сила тока/Напряжение/Мощность#  - слишком большое - ОСТЕРЕГАЙТЕСЬ ЭТИХ ЗНАЧЕНИЙ!!!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("############################################################################################################################")


