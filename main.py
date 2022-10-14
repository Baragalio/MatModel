import Data as данные
import Utils
import matplotlib.pyplot as plt
from Functions import dC1
from Localizate import Вывести, РассчитатьПоЭйлеру

C, t = РассчитатьПоЭйлеру(Utils.Cu(20, 0.3), dC1,0.01, 0, 10)

fig, ax = plt.subplots()
ax.grid()
plt.title("C1")
ax.set_ylabel("С1")
ax.set_xlabel("t ")
#ax.scatter(t_mas, C_out_mas,s=2,color="red")
Вывести(len(C))
Вывести(len(t))
ax.plot(C, t,color="green",alpha=0.3)
plt.show()