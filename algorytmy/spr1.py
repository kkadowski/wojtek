'''
Wczytanie z pliku o nazwie plik.txt liczb i wypisanie liczb, 
których suma cyfr podniesiona do potęgi 2 daje liczbę nieparzystą.
Wypisz te liczby w porządku rosnącym wraz z indeksami w pliku.

1. wczytanie i zwrócenie listy liczb
2. f. do sprawdzania czy suma ^2 jest nieparzysta
3. tworzenie słownika liczba spełniajaca warunek + położenie w pliku
4. posortawać słownik wg wartości liczby

'''

def wczytywanie(plik = "plik.txt", tryb = "rt"):
    try:
        with open(plik, tryb) as file:
            linie = [f.replace("\n", "") for f in file.readlines()]
        return linie
    except FileNotFoundError as er:
        print(f"Problem z odczytem pliku {plik}...")
        return 0

def sprawdz_warunek(lista):
    slownik = dict()
    for i in range(len(lista)):
        suma = 0
        for j in range(len(lista[i])):
            suma += int((lista[i])[j])**2
        if suma % 2 != 0:
            slownik[lista[i]]= i+1
    return slownik  

def sortuj(slownik):
    return dict(sorted(slownik.items(), key = lambda x: x[0]))

#==========================
def main():
    lista = wczytywanie("testowy.txt")
    slownik_spelniajacych = sprawdz_warunek(lista)
    slownik_posortowany = sortuj(slownik_spelniajacych)
    print(slownik_posortowany)
    
main()



