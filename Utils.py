import math
import Data

def k(A, E):
    return A * math.exp(-E / (Data.R * Data.T))

# Концентрация из % в моль/м3
def M(C, u):
    return (C * Data.p) / (100 * u)

