import math
import Data

def k(A, E):
    return A * math.exp(-E / (Data.R * Data.T))

# Концентрация из % в моль/м3
def Cu(C, u):
    return (C * Data.p) / (100 * u)

def S():
    return math.pi * Data.D ** 2 / 4
