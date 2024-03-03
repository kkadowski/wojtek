'''!
Zad. 1 Wygeneruj 1000 wyrazów pisanych małymi literami o długościach
od 5 do 10 znaków i zapisz je w pliku wyrazy.txt.
Odczytaj wyrazy z pliku i sprawdź ile wyrazów ma poszczególne długości.
Wykonaj histogram z ilości wyrazów o poszczególnych długościach.
'''
from random import randint as rdi
import matplotlib.pyplot as plt

def generuj():
    wyrazy = []
    for i in range(1000):
        dl = rdi(5,10)
        wyraz = ''
        for i in range(dl):
            wyraz += chr(rdi(97,122))
        wyrazy.append(wyraz)
    return wyrazy

def zapis(wyrazy):
    try:
        with open("wyrazy.txt","w+t") as f:
            for wyraz in wyrazy:
                f.write(wyraz + '\n')
    except FileNotFoundError:
        print("Plik nie istnieje...")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd {e}")

def odczyt(plik):
    staty = dict()
    try:
        with open(plik, "r+t") as f:
            wyrazy = f.readlines()
            wyrazy = [ wyraz.replace("\n","") for wyraz in wyrazy ]
            for wyraz in wyrazy:
                if len(wyraz) in staty:
                    staty[len(wyraz)] += 1
                else:
                    staty[len(wyraz)] = 1
            return staty
    except FileNotFoundError:
        print("Plik nie istnieje...")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd {e}")
        
        
        
def histogram(staty):
    print(staty)
    staty_sorted = dict(sorted(staty.items()))
    print(staty_sorted)
    plt.bar(staty_sorted.keys(), staty_sorted.values(), align='center')
    plt.title("Ilość wystąpień liczb")
    plt.xlabel("Liczby")
    plt.ylabel("Ilosć wystąpień")
    plt.show()  
   
def main():
    zapis(generuj())
    staty = odczyt("wyrazy.txt")
    histogram(staty)

# ----------------------------MAIN --------------------

if __name__ == "__main__":
    main()
    

