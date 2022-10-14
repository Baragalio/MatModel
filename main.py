import Data
import Data as данные
import Utils
import matplotlib.pyplot as plt
from Functions import dC1, dC2, dC3
from Localizate import Вывести, РассчитатьПоЭйлеру

print(dC1(Utils.Cu(20.0, Data.u1)))
C, t = РассчитатьПоЭйлеру(Utils.Cu(20.0, Data.u1), dC1, 0.01, 0, 5)


print(Utils.Cu(20.0, Data.u1))
print(Utils.U())
print(Utils.k(Data.A1, Data.E1))
fig, ax = plt.subplots()
ax.grid()
plt.title("C1")
ax.set_ylabel("С1")
ax.set_xlabel("t")
#ax.scatter(t_mas, C_out_mas,s=2,color="red")
ax.plot(t, C, color="green", alpha=0.3)
plt.show()