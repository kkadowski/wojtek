'''
Liczby doskonałe
K>K> 2023
'''

def czy_dosk(n):
    suma = 1   # każda dzieli się przez 1 więc od razu dodajemy
    k = 2 # zaczynamy od drugiej liczby
    while k**2 <= n: #warunek końcowy
        if n % k == 0:
            suma += k + (n / k) # dodajemy dzielnik i drugi będący parą w odpowiedzi na dzielenie
                                # np. dla 6 dzielnikiem jest 2 ale i zarazem 6/2 = 3 i też jest dzielnikiem
        k += 1
    return suma == n
    


n = int(input("Podaj liczbę: "))
if czy_dosk(n):
    print(f"Liczba {n} jest doskonała.")
else:
    print(f"Liczba {n} nie jest doskonała.")