import Data
from Utils import k


def dC1(C1):
    return - k(Data.A1, Data.E1) * C1 / Data.V


def dC2(C1, C2):
    return (k(Data.A1,Data.E1) * C1 - k(Data.A2, Data.E2) - k(Data.A4, Data.E2) * C2) / Data.V


def dC3(C2, C3):
    return (k(Data.A2, Data.E2) * C2 - k(Data.A3, Data.E3) * C3) / Data.V


def dC4(C2, C3):
    return (k(Data.A3, Data.E3) * C3 + k(Data.A4, Data.E4) * C2) / Data.V