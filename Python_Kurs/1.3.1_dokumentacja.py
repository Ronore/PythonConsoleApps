# Zmienne globalne używane w rozszerzonym algorytmie Euklidesa
global x
global y
x = 1
y = 0


def sprawdz_pierwszosc(n):
    """
    Funkcja sprawdza, czy podana liczba n jest liczbą pierwszą.

    Parametry:
    n (int): Liczba do sprawdzenia

    Zwraca:
    bool: True, jeśli liczba jest pierwsza, False w przeciwnym razie
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def szybkie_potengowanie(podstawa, moc):
    """
    Funkcja implementuje szybkie potęgowanie metodą dzielenia wykładnika na pół.

    Parametry:
    podstawa (int): Liczba, która ma być potęgowana
    moc (int): Wykładnik potęgi

    Zwraca:
    int: Wynik potęgowania
    """
    if moc == 0:
        return 1
    elif moc % 2 == 1:
        return podstawa * szybkie_potengowanie(podstawa, (moc - 1))

    w = szybkie_potengowanie(podstawa, moc / 2)
    return w * w


def algorytm_euklidesa(liczba1, liczba2):
    """
    Funkcja implementuje klasyczny algorytm Euklidesa do obliczania NWD (największego wspólnego dzielnika).

    Parametry:
    liczba1 (int): Pierwsza liczba
    liczba2 (int): Druga liczba

    Zwraca:
    int: Największy wspólny dzielnik
    """
    while liczba1 != liczba2:
        if liczba1 > liczba2:
            liczba1 -= liczba2
        else:
            liczba2 -= liczba1
    return liczba1


def rozszerzony_euklides(liczba1, liczba2):
    """
    Funkcja implementuje rozszerzony algorytm Euklidesa, który pozwala na znalezienie współczynników x i y
    w równaniu Diofantycznym: ax + by = NWD(a, b).

    Parametry:
    liczba1 (int): Pierwsza liczba
    liczba2 (int): Druga liczba

    Zwraca:
    Brak wartości zwracanej, ale modyfikuje globalne zmienne x i y.
    """
    if liczba2 != 0:
        global y
        global x
        rozszerzony_euklides(liczba2, liczba1 % liczba2)
        pom = y
        y = x - (liczba1 // liczba2) * y
        x = pom


# Tworzenie listy zawierającej liczby 10*i + j dla i od 1 do 9 oraz j od 0 do i
listax = [10 * i + j for i in range(1, 10) for j in range(0, i)]

# Wypisanie elementów listy
for i in listax:
    print(i)

# Sprawdzenie pierwszości liczby 8
if sprawdz_pierwszosc(8):
    print("Jest pierwsza")
else:
    print("Nie jest pierwsza")

# Obliczenie 16^2 metodą szybkiego potęgowania
print(szybkie_potengowanie(16, 2))

# Obliczenie NWD(20,2) za pomocą algorytmu Euklidesa
print(f"Największy wspólny dzielnik to: {algorytm_euklidesa(20, 2)}")

# Obliczenie rozszerzonego algorytmu Euklidesa dla 13 i 5
rozszerzony_euklides(13, 5)

# Wypisanie wartości y po wykonaniu rozszerzonego algorytmu Euklidesa
print(y)
