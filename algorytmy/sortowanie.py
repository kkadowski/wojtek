'''
Metody sortowania liczb
K>K> 2023
'''

from measuertime import measuretime as mt
from random import randint as rdi
import os


metody = {'b': "bubblesort", 'i': "insertsort", 's':"selectionsort", 'q':"quicksort"}
#czyszczenie ekranu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# menu
def menu():
    clear_screen()
    print("""
        Metody sortowania: 
        b - bubblesort,
        i - insersort,
        s - selectionsort,
        q - quicksort 
    """)
    
# powitanie
def powitanie():
    print("\n")
    print("=" * 50)
    print("Aplikacja do sortowania liczb")
    print("=" * 50)
    print("\n")
 
# generaot liczb   
def generator():
    while True:
        try:
            n = int(input("Podaj ilość liczb n="))
            d = int(input("Podaj dolny zakres liczb d="))
            g = int(input("Podaj górny zakres liczb g="))
            if d > g: d, g = g, d
            liczby = [ rdi(d,g) for i in range(n) ]
            return liczby
        except ValueError:
            print("Miałeś podać liczby...")

# zapis do pliku
def zapis(liczby, plik, tryb="at", czas = -1, metoda=''):
    try:
        with open(plik, tryb) as f:
            if metoda == '':
                f.write ("-" * 30)
                f.write("\nLiczby nieposortowane: \n")
            [ f.write(str(liczba)+" : ") for liczba in liczby ]
            f.write("\n")
            if czas != -1:
                f.write(f"Czas wykonania [{metody[metoda]}]: " + str(czas)+"\n")
    except FileNotFoundError:
        print(f"Plik {plik} nie istnieje.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

def czyzapis():
    czy = ''
    while czy not in ['t','T', 'n', 'N']:
        czy = input("Czy chcesz zapisać? (t/n)")

    if czy in ['t', 'T']:
        return True
    else:
        return False
        



# sortowanie bąblekowe
@mt
def sort_bubble(liczby):
    for i in range(len(liczby)):
        for j in range(len(liczby) -1):
            if liczby[j] > liczby[j+1]:
                #liczby[j], liczby[j+1] = liczby[j+1], liczby[j] # python like
                temp = liczby[j]
                liczby[j] = liczby[j+1]
                liczby[j+1] = temp
    return liczby

#sortowanie przez wstawianie
@mt
def sort_insert(liczby):
    for i in range(1, len(liczby)):
        j = i
        while liczby[j] < liczby[j-1] and j > 0:
            liczby[j], liczby[j-1] = liczby[j-1], liczby[j]
            j -= 1
    return liczby

@mt
def sort_selection(liczby):
    for i in range(len(liczby)):
        min = i
        for j in range(i, len(liczby)):
            if liczby[min] > liczby[j]:
                min = j
        liczby[i], liczby[min] = liczby[min], liczby[i]
    return liczby


@mt
def sort_quick(liczby):
    return quick(liczby)
    
# rekurencja
def quick(liczby):
    if len(liczby) <=1:
        return liczby
    pivot = liczby[len(liczby) // 2]  # metoda dziel i zwyciężaj
    left = [ x for x in liczby if x < pivot ]
    middle = [ x for x in liczby if x == pivot ]
    right = [ x for x in liczby if x > pivot ]
    return quick(left) + middle + quick(right)
   
 
#wyświetlanie liczb   
def show(liczby, when = True, se_time = 0):
    if when == True:
        print("\n Liczby przed sortowaniem: \n")
        print(liczby)
    else:
        print("\n Liczby po sortowaniu: \n")
        print(liczby)
        print(f"\n Sortowanie trwało: {se_time} s. \n")
    
# ============= MAIN ==============
def main():
    powitanie()
    czygen = True
    se_time = 0
    liczby = []
    while True:
        
        if czygen == True:
            liczby = generator()   
            if czyzapis():
                zapis(liczby, 'sorty.txt', tryb="at", czas = -1, metoda = '')
         
        menu()
        sort = ''
        while sort not in metody.keys():
            sort = input("Wybierz metodę sortowania: ") 
            posortowane = []
            
            if sort =='b':
                liczby_c = liczby.copy()
                show(liczby, True)
                posortowane, se_time = sort_bubble(liczby_c)
                show(posortowane, False, se_time)                                    
            elif sort == 'i':
                liczby_c = liczby.copy()
                show(liczby, True)
                posortowane, se_time = sort_insert(liczby_c)
                show(posortowane, False, se_time)
            elif sort == 's':
                liczby_c = liczby.copy()
                show(liczby, True)
                posortowane, se_time = sort_selection(liczby_c)
                show(posortowane, False, se_time)
            elif sort == 'q':
                liczby_c = liczby.copy()
                show(liczby, True)
                posortowane, se_time = sort_quick(liczby_c)
                show(posortowane, False, se_time)
            if czyzapis():
                zapis(posortowane, 'sorty.txt', tryb="at", czas = se_time, metoda = sort )    
                
        koniec =''
        while koniec not in ['t','T','n','N']:
            koniec = input("Czy chcesz kontynuować? (t/n) ")
        
        if koniec not in ['t', 'T']:
            break
        else:
            wyb =''
            while wyb not in ['t','T','n','N']:
                wyb = input("Czy chcesz wygenerować nowe liczby? (t/n) ")
                
            if wyb in ['t','T']:
                czygen = True
            else:
                czygen = False
                
    clear_screen()    
    print("\n Dziękujemy za współpracę...\n ")
    
if __name__ == "__main__":
    main()