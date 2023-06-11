# # Napisać program który wyświetla wykres funkcji kwadratowej o podanych współczynnikach.

# # Tworząc wykres należy tak dobrać zakres wyświetlanej osi X aby znalazły się w nim: 
# # współrzędna wierzchołka oraz miejsca zerowe z marginesem ok 10% 
# # (dla przykładu: jeżeli miejsca zerowe wynoszą np x1=2 i x2=10 to oś X powinna zawierać punkty od 1.8 do 11). 
# # Jeżeli parabola nie ma miejsc zerowych, lub ma podwójne miejsce zerowe, wykres powinien zawierać wierzchołek paraboli oraz margines ok 20% 
# # (dla przykładu jeżeli wsp. wierzchołka wynosi x0=5 to oś X powinna zawierać punkty od  4 do 6).
import math
import matplotlib.pyplot as plot
import numpy as np

def liczenie_delty(a,b,c):
    delta = (b*b) - 4*(a*c)
    print('delta =',delta)
    return delta

def wykres(delta,a,b,c):
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
        x0 = None
    else : print('Równanie nie ma rozwiązań')
    print("f(x)={0}x^2+{1}x+{2}".format(a,b,c))
    p = (-b)/(2*a)
    q = (-delta)/(4*a)
    print('p',p,'q',q)
    if x0 is None:
        if x1>x2:
            x = np.linspace(x1+(0.1*x1), x2-(0.1*x1), 1000)
            y = a * x ** 2 + b * x + c
            fig, ax = plot.subplots()
            ax.set_title("Wykres funkcji kwadratowej")
            plot.grid(True)
            ax.plot(x, y)
            ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
            plot.scatter(p, q, color='red', label='Wierzchołek')
            if x1 is not None:
                plot.scatter(x1, 0, color='green', label='Miejsce zerowe')
            if x2 is not None:
                plot.scatter(x2, 0, color='green', label='Miejsce zerowe')
            plot.show()
        else:
            x = np.linspace(x1-(0.1*x1), x2+(0.1*x1), 1000)
            y = a * x ** 2 + b * x + c
            fig, ax = plot.subplots()
            ax.set_title("Wykres funkcji kwadratowej")
            plot.grid(True)
            ax.plot(x, y)
            ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
            plot.scatter(p, q, color='red', label='Wierzchołek')
            if x1 is not None:
                plot.scatter(x1, 0, color='green', label='Miejsce zerowe')
            if x2 is not None:
                plot.scatter(x2, 0, color='green', label='Miejsce zerowe')
            plot.show()
    else:
        x = np.linspace(x0-(0.2*x0), x0+(0.2*x0), 1000)
        y = a * x ** 2 + b * x + c
        fig, ax = plot.subplots()
        ax.set_title("Wykres funkcji kwadratowej")
        plot.grid(True)
        ax.plot(x, y)
        ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)
        plot.scatter(p, q, color='red', label='Wierzchołek')
        plot.show()

print('Podaj liczbę a:')
a=input()
while a == '0':
    print('a musi być liczbą całkowitą ani być równe zero. Podaj liczbę a jeszcze raz:')
    a=input()
a = int(a)

print('Podaj liczbę b:')
b=input()
b = int(b)

print('Podaj liczbę c:')
c=input()
c = int(c)

delta = liczenie_delty(a,b,c)
wykres(delta,a, b, c)
