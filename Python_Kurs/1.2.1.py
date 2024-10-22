import math

def quadraticformula(a, b, c):
    delta = (b * b) - (a * c * 4)
    if delta > 0:
        delta = math.sqrt(delta)
        result1 = (delta - b) / 2
        result2 = (-delta - b) / 2
        return result1, result2

wspa = abs(complex(input("Podaj współczynik A: ")))
wspb = abs(complex(input("Podaj współczynik B: ")))
wspc = abs(complex(input("Podaj współczynik C: ")))

print(quadraticformula(wspa, wspb, wspc))
