def multi(v1:list[float],v2:list[float])->list[float]:
    v3 = []
    for i in range(len(v1)):
        num1 = v1[i]
        num2 = v2[i]
        v3.append(num1*num2)
    return v3

def skal_multi(v1: list[float], s: float):
    v2 = []
    for i in range(len(v1)):
        v2.append(v1[i] * s)
    return v2