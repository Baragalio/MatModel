import math
from Data.Data import p, R, T, V, D


def k(A, E):
    return A * math.e ** (-CalToDj(E) / (R * T))


# Концентрация из % в моль/м3
def CtoM(C, u):
    return (C * p) / (100 * u)
def MtoC(M, u):
    return M * 100 * u / p


def S():
    return math.pi * D ** 2 / 4


def U():
    return V / (math.pi * S())


def CalToDj(E):
    return E / 0.23900573613767
