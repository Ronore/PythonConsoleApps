a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

def algorytmEuklidesa(a, b):
    while True:
        if a != b:
            if a > b:
                a -= b
            else:
                b -= a
        else:
            return a


print(algorytmEuklidesa(a, b))

