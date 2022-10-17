from matplotlib import pyplot as plt

import Data.Data as данные
from Functionality.Euler import Eulers
from MetodParabol import additional
from Localizate import РассчитатьПоЭйлеру4С, отрисоватьCdl, ЗадатьНачальныеПараметры, КонвертCвM, КонвертMвC

НачальныеПараметры = ЗадатьНачальныеПараметры(КонвертCвM(20.0, данные.µ1), 0, 0, 0)
j = Eulers(НачальныеПараметры, 0.01, 0)
C1, C2, C3, C4, l = РассчитатьПоЭйлеру4С(НачальныеПараметры, 0.0001, 0, 5)
x1 = 0
x2 = 2
x3 = 3
print(j.GetEuler3C(0))
print(j.GetEuler3C(4))
print(j.GetEuler3C(6))
print()

print(additional.Xmin(x1, x2, x3, j.GetEuler3C))

fig, ax = plt.subplots()
ax.grid()
plt.title("C/dl")
ax.set_ylabel("С")
ax.set_xlabel("l")

ax.plot(l, C1, color="green", alpha=0.3, label="C1")
ax.plot(l, C2, color="orange", alpha=0.3, label="C2")
ax.plot(l, C3, color="red", alpha=0.3, label="C3")
ax.plot(l, C4, color="black", alpha=0.3, label="C4")
ax.scatter(x1, j.GetEuler3C(x1))
ax.scatter(x2, j.GetEuler3C(x2))
ax.scatter(x3, j.GetEuler3C(x3))
ax.scatter(additional.Xmin(x1, x2, x3, j.GetEuler3C), j.GetEuler3C(additional.Xmin(x1, x2, x3, j.GetEuler3C)))

plt.legend()
plt.show()

