# Napisać program, który sprawdza czy wprowadzona z wejścia liczba jest liczbą pierwszą. Samo sprawdzenie liczby pierwszej ma być zrealizowane za pomocą funkcji.

# Wewnątrz tej funkcji nie wolno używać input() i print()
import math

def liczba_pierwsza(liczba):
    if liczba < 2:
        return 'Liczba nie jest liczbą pierwszą' # Liczba pierwsza musi być wyższa od 1
    for dzielnik in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % dzielnik == 0:
            return 'Liczba nie jest liczbą pierwszą'
    return 'Liczba jest liczbą pierwszą'
    
    

liczba=int(input())
rezultat=liczba_pierwsza(liczba)
print(rezultat)