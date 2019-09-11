# coding: utf-8

import random

a = 1
b = 10
ran = random.randrange(a, b)

print ("Какое число я загадал???  ", a, 'или', b)
question = 0

while question != ran:
    question = int(input())
    if question == ran:
        print("        ")
        print("Ты выиграл!!!!!!!!!!!")
        print("Ты выиграл!!!!!!!!!!!")
        print("Ты выиграл!!!!!!!!!!!")

    elif question > ran:
        print("        ")
        print("Меньше!!!")

    elif question < ran:
        print("        ")
        print("Больше!!!")






