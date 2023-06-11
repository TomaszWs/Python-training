# Napisać funkcję, która otrzymuje kartezjańskie (x,y) współrzędne punktu  na płaszczyźnie a zwraca współrzędne tego punktu w układzie biegunowym (długość, kąt)

# Wewnątrz tej funkcji nie wolno używać print() i input()
import math

def zamiana(x,y):
    r = math.sqrt(x**2+y**2)
    kat=math.degrees(math.atan2(y,x))
    dane = {'r':r,'kąt':kat}
    return dane

x = int(input())
y = int(input())
wynik = zamiana(x,y)
print(wynik)