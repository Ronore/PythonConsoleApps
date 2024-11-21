global x
global y
x = 1
y = 0

def sprawdz_pierwszosc(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def szybkie_potengowanie(podstawa, moc):
    if moc == 0:
        return 1
    elif moc % 2 == 1:
        return podstawa * szybkie_potengowanie(podstawa, (moc - 1))

    w = szybkie_potengowanie(podstawa, moc / 2)
    return w * w

def algorytm_euklidesa(liczba1, liczba2):
    while liczba1 != liczba2:
        if liczba1 > liczba2:
            liczba1 -= liczba2
        else:
            liczba2 -= liczba1
    return liczba1


def rozszerzony_euklides(liczba1, liczba2):
    if liczba2 != 0:
        global y
        global x
        rozszerzony_euklides(liczba2,liczba1%liczba2)
        pom = y
        y = x - liczba1//liczba2*y
        x = pom

listax = [10*i+j for i in range(1,10) for j in range(0,i)]
for i in listax:
    print(i)

if sprawdz_pierwszosc(8):
    print("Jest pierwsza")
else:
    print("Nie jest pierwsza")

print(szybkie_potengowanie(16, 2))
print(f"Największy wspólny dzielnik to: {algorytm_euklidesa(20, 2)}")
rozszerzony_euklides(13,5)
print(y)


