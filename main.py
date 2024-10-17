peselString = input("Wpisz swój numer PESEL: ")
peselTablica = []

if len(peselString) != 11 or not peselString.isnumeric():
    peselTablica = [5, 5, 0, 3, 0, 1, 0, 1, 1, 9, 3]
else:
    for i in peselString:
        peselTablica.append(int(i))


def sprawdzPlec(PESEL):
    if PESEL[9] % 2 == 0:
        return "Kobieta"
    else:
        return "Mężczyzna"


def sprawdzPoprawnoscKontrolnej(PESEL):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S = 0
    for i in range(10):
        S += PESEL[i] * wagi[i]
    M = S % 10
    if M == 0:
        R = 0
    else:
        R = 10 - M
    if R == PESEL[10]:
        return True
    else:
        return False


print(sprawdzPlec(peselTablica))
print(sprawdzPoprawnoscKontrolnej(peselTablica))
