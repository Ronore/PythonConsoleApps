def sprawdzpierwszosc(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def szybkiepotengowanie(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return x * szybkiepotengowanie(x, (n - 1))

    w = szybkiepotengowanie(x, n/2)
    return w * w

if sprawdzpierwszosc(8):
    print("Jest pierwsza")
else:
    print("Nie jest pierwsza")

print(szybkiepotengowanie(16, 7))