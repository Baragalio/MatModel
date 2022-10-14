import numpy as np


def CountEuler(C0, dC, delta, min, max):
    C = [C0]
    IntSteps = [min]
    for h in np.arange(min, max, delta):
        C0 = C0 + dC(C0) * delta

        C.append(C0)
        IntSteps.append(h)
    return C, IntSteps