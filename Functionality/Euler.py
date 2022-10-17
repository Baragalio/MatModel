import numpy as np

from Data.DataPacket import Begin4C
from Functionality.Functions import dC1, dC2, dC3, dC4


class Eulers():
    def __init__(self, begin4C, delta, initVal):
        self.begin4C = begin4C
        self.delta = delta
        self.initVal = initVal
    def GetEuler3C(self, count):
        dbegin4C = Begin4C(self.begin4C.C1, self.begin4C.C2,
                           self.begin4C.C3, self.begin4C.C4)
        for h in np.arange(self.initVal, count, self.delta):
            dbegin4C.C1 = dbegin4C.C1 + dC1(dbegin4C.C1) * self.delta
            dbegin4C.C2 = dbegin4C.C2 + dC2(dbegin4C.C1, dbegin4C.C2) * self.delta
            dbegin4C.C3 = dbegin4C.C3 + dC3(dbegin4C.C2, dbegin4C.C3) * self.delta
        return dbegin4C.C3

def EulerC4(begin4C, delta, min, max):
    C1m = [begin4C.C1]
    C2m = [begin4C.C2]
    C3m = [begin4C.C3]
    C4m = [begin4C.C4]
    hm = [min]
    for h in np.arange(min, max, delta):
        C1m.append(C1m[-1] + dC1(C1m[-1]) * delta)
        C2m.append(C2m[-1] + dC2(C1m[-1], C2m[-1]) * delta)
        C3m.append(C3m[-1] + dC3(C2m[-1], C3m[-1]) * delta)
        C4m.append(C4m[-1] + dC4(C2m[-1], C3m[-1]) * delta)
        hm.append(h)
    return C1m, C2m, C3m, C4m, hm

def GetEuler3C(begin4C, delta, count):
    for h in np.arange(0, count, delta):
        begin4C.C1 = begin4C.C1 + dC1(begin4C.C1) * delta
        begin4C.C2 = begin4C.C2 + dC2(begin4C.C1, begin4C.C2) * delta
        begin4C.C3 = begin4C.C3 + dC3(begin4C.C2, begin4C.C3) * delta
    return begin4C
def StepEuler(C, dC, delta):
    return 0 + dC(C) * delta


def CountEuler(C0, dC, delta, min, max):
    C = [C0]
    IntSteps = [min]
    for h in np.arange(min, max, delta):
        C0 = C0 + dC(C0) * delta
        C.append(C0)
        IntSteps.append(h)
    return C, IntSteps