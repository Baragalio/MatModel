import Data.Data as данные

import Utils
from Functionality.Euler import Eulers
from Localizate import РассчитатьПоЭйлеру4С, отрисоватьCdl, ЗадатьНачальныеПараметры, КонвертCвM, КонвертMвC

НачальныеПараметры = ЗадатьНачальныеПараметры(КонвертCвM(20.0, данные.µ1), 0, 0, 0)

j = Eulers(НачальныеПараметры, 0.01, 0)
print(j.begin4C.C3)
print(j.GetEuler3C(1))
print(j.begin4C.C3)


C1, C2, C3, C4, l = РассчитатьПоЭйлеру4С(НачальныеПараметры, 0.0001, 0, 5)
print(str(l[C3.index(max(C3))]) + " м")
print(str(КонвертMвC(max(C3), данные.µ3)) + " моль/м3")
отрисоватьCdl(C1, C2, C3, C4, l)



