# Napisać funkcję, która zwraca długość wektora (w 3 wymiarach). Wektor ma być przesłany do funkcji jako:

# a) trzy niezależne współrzędne,

# b) lista,

# c) słownik,
# Wewnątrz funkcji nie wolno używać print() i input()

import math
# a) 
def dlugosc_wektor(x,y,z):
    dlugosc = math.sqrt((x*x)+(y*y)+(z*z))
    return dlugosc

x = 1
y = 2
z = 3
wynik = dlugosc_wektor(x,y,z)
print('Długość wektora po współrzędnych:',wynik)

# b)
def dlugosc_wektor_v2(wspolrzedne):
    dlugosc_v2 = math.sqrt((wspolrzedne[0]**2)+wspolrzedne[1]**2+wspolrzedne[2]**2)
    return dlugosc_v2
wspolrzedne = [1,2,3]
wynik_v2 = dlugosc_wektor_v2(wspolrzedne)
print('Długość wektora według listy:',wynik_v2)

# c)
def dlugosc_wektor_v3(slownik):
    dlugosc_v3 = math.sqrt(slownik['x']**2+slownik['y']**2+slownik['z']**2)
    return dlugosc_v3

slownik = {'x':1,'y':2,'z':3}
wynik_v3 = dlugosc_wektor_v3(slownik)
print('Długość wektora według słownika:',wynik_v3)