# coding: utf-8
print("        ")
print("###############################")
print("Электронный коллега 1.0v")
print("Автор: Дмитрий Павлухин")
print("###############################")

import numpy as np
import matplotlib.pyplot as plt
import math

# перевод из градусов в радианы


t = np.arange(0.0, 1.0, 0.009)
s = np.sin(2 * np.pi * t)

upper = 0.90
lower = -0.86

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)


fig, ax = plt.subplots()
ax.grid
ax.plot(t, smiddle,'k', t, slower, 'r',  t, supper,'g')
fig.savefig("result.png")
plt.show()
