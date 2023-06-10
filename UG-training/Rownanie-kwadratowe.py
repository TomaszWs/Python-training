# Napisać program, który umożliwia znalezienie rozwiązania równania kwadratowego.

# Współczynniki równania mają być przechowywane w postaci listy.

# Obliczenie wartości delty ma być zrealizowane za pomocą dodatkowej funkcji.

# Należy rozpatrzyć trzy przypadki: delty większej od zera, delty równej zero i mniejszej od  zera. 


import math

def liczenie_delty(a,b,c):
    delta = (b*b) - 4*(a*c)
    print('delta =',delta)
    return delta

def miejsca_zerowe(delta,a,b):
    if delta == 0 :
        print('Równanie ma jedno rozwiązanie')
        x0 = (-b-(math.sqrt(delta)))/(2*a)
        print('x0 =',x0)
    elif delta > 0 :
        print('Równanie ma dwa rozwiązanie')
        x1 = (-b-(math.sqrt(delta)))/(2*a)
        x2 = (-b+(math.sqrt(delta)))/(2*a)
        print('x1 =',x1)
        print('x2 =',x2)
    else : print('Równanie nie ma rozwiązań') # Rozwiązanie dla delty mniejszej od zera

print('Podaj liczbę a:')
a=input()
while not a.isdigit() :
    print('a musi być liczbą całkowitą oraz nie może być równe zero. Podaj liczbę a jeszcze raz:')
    a=input()
while a == '0':
    print('a musi być liczbą całkowitą ani być równe zero. Podaj liczbę a jeszcze raz:')
    a=input()
a = int(a)

print('Podaj liczbę b:')
b=input()
while not b.isdigit() :
    print('b musi być liczbą całkowitą. Podaj liczbę b jeszcze raz:')
    b=input()
b = int(b)

print('Podaj liczbę c:')
c=input()
while not c.isdigit():
    print('c musi być liczbą całkowitą. Podaj liczbę c jeszcze raz:')
    c=input()
c = int(c)

linia = 'Równanie ma postać {}x^2+{}x+{}=0'.format(a,b,c)
print(linia)
delta = liczenie_delty(a,b,c)
miejsca_zerowe(delta,a,b)