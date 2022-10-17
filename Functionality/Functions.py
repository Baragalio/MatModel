from Data.Data import A1, A2, A3, A4, E1, E2, E3, E4
from Utils import k, U

def dC1(C1):
    return - k(A1, E1) * C1 / U()


def dC2(C1, C2):
    return (k(A1, E1) * C1 - k(A2, E2) * C2 - k(A4, E4) * C2) / U()


def dC3(C2, C3):
    return (k(A2, E2) * C2 - k(A3, E3) * C3) / U()


def dC4(C2, C3):
    return (k(A3, E3) * C3 + k(A4, E4) * C2) / U()