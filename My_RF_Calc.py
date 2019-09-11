# coding: utf-8



dBm = 0
i = 'Y'
while i != 'N':

    if i == 'Y':
        print("        ")
        dBm = int(input("Введите dBm >>>  "))
        a = dBm / 10
        b = 10 ** a
        c = b / 1000

        print("Введено: ", dBm, "dBm")
        print("МиллиВатт: ","%.3f" % b, "mW")
        print("Ватт: ","%.4f" % c, "W")

