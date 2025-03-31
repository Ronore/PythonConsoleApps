# Algorytmy Matematyczne w Pythonie

Ten projekt zawiera implementację kilku podstawowych algorytmów matematycznych, w tym:
- Sprawdzanie, czy liczba jest pierwsza
- Szybkie potęgowanie
- Algorytm Euklidesa do obliczania NWD (Największego Wspólnego Dzielnika)
- Rozszerzony algorytm Euklidesa

## 📜 Opis funkcji

### `sprawdz_pierwszosc(n)`
Sprawdza, czy liczba `n` jest liczbą pierwszą.

**Parametry**:
- `n` (int): Liczba do sprawdzenia

**Zwraca**:
- `True`, jeśli liczba jest pierwsza
- `False`, jeśli liczba nie jest pierwsza

---

### `szybkie_potengowanie(podstawa, moc)`
Implementacja szybkiego potęgowania metodą dzielenia wykładnika na pół.

**Parametry**:
- `podstawa` (int): Podstawa potęgowania
- `moc` (int): Wykładnik potęgi

**Zwraca**:
- Wynik potęgowania (`podstawa^moc`)

---

### `algorytm_euklidesa(liczba1, liczba2)`
Oblicza największy wspólny dzielnik (NWD) dwóch liczb metodą klasycznego algorytmu Euklidesa.

**Parametry**:
- `liczba1` (int): Pierwsza liczba
- `liczba2` (int): Druga liczba

**Zwraca**:
- Największy wspólny dzielnik dwóch liczb

---

### `rozszerzony_euklides(liczba1, liczba2)`
Rozszerzona wersja algorytmu Euklidesa, pozwalająca znaleźć współczynniki x i y w równaniu Diofantycznym:  
`a * x + b * y = NWD(a, b)`

**Parametry**:
- `liczba1` (int): Pierwsza liczba
- `liczba2` (int): Druga liczba

**Zwraca**:
- Zmodyfikowane globalne zmienne `x` i `y`, które są rozwiązaniem równania

---

## 🔧 Jak uruchomić program?
1. Pobierz plik `main.py` (lub inny plik, w którym znajduje się kod).
2. Upewnij się, że masz zainstalowanego Pythona (wersja 3.x).
3. Otwórz terminal lub wiersz poleceń i uruchom skrypt:


