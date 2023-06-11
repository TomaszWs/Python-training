# Napisać funkcję, która na podstawie przesłanej do niej listy znajdzie największą liczbę.

# Pokazać działanie tej funkcji w prostym programie.

# Wewnątrz tej funkcji nie wolno używać print() i input()

def naj_liczba(lista):
    lista.sort(reverse = True)
    najwieksza = lista[0]
    return najwieksza

def naj_liczba_v2(lista):
    najwieksza_liczba = lista[0]
    for i in range(len(lista)):
        if lista[i] > najwieksza_liczba:
            najwieksza_liczba = lista[i]
    return najwieksza_liczba

lista = [1,2,3,4,5,100,232,45,233,54,754]
poszukiwana_liczba = naj_liczba(lista)
print('Największa liczba znaleziona przez sortowanie:',poszukiwana_liczba)

poszukiwana_liczba = naj_liczba_v2(lista)
print('Największa liczba w zbiorze:',poszukiwana_liczba)