# Napisać funkcję która na podstawie przesłanych do niej wartości znajduje ich największy wspólny podzielnik.

# Pokazać działanie tej funkcji w prostym programie

# Wewnątrz funkcji nie wolno używać print() i input()

def nwd(a,b):
    while b != 0:
        c = b
        b = a%b
        a = c
    return a

a = int(input())
b = int(input())
rezultat = nwd(a,b)
print(rezultat)
