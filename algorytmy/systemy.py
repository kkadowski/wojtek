'''
Zamiana systemów bin, dec, oct, hex
K>K>
'''

def bin2dec():
    print("\nJesteś w zamianie systemu binarnego do dziesiętnego..\n")
    liczba_bin = input("Podaj liczbę binarną: ")
    # todo sprawdzić czy rzeczywiście jest binarna (czy są 0 i 1)
    liczba_bin = liczba_bin[::-1]   # odwracamy kolejność binarnej
    dl = len(liczba_bin)            # sprawdzamy długość
    liczba_dec = 0
    for i in range(dl):
        liczba_dec += int(liczba_bin[i])*(2**i)
    print(f"Liczba binarna {liczba_bin} to w systemie dziesiętnym liczba {liczba_dec}.\n")

def dec2other():
    print("Jesteś w zamianie systemu dziesiętnego do dowolnego...")
    hex = ["A", "B", "C", "D", "E", "F"]
    
    liczba_dec = input("Podaj liczbę dziesiętną: ")
    podst = int(input("Podaj podstawę systemu: "))
    if int(liczba_dec) != 0:
        l = int(liczba_dec)
        reszta = 0
        liczba = ''
        while l != 0:
            reszta = l % podst
            if reszta > 9:
                liczba += str(hex[reszta-10])
            else:
                liczba += str(reszta)
            l //= podst
        liczba = liczba[::-1]
        print(f"Liczba dziesiętna {liczba_dec} w systemie o podstawie\n {podst} to liczba {liczba}. \n")
 
       
                    
def wstep():
    print("=" * 50)
    print("Przeliczanie systemów")
    print("=" * 50)


def menu():
    print("""Menu:  
          b - bin2dec,
          d - dec do dowolnej,
          """)

def main():
    wybor = ''
    wstep()
    
    while True:
        menu()
        wybor = input("Wybierz co chcesz robić: ")
        if wybor in ['b', 'd']:
            if wybor == 'b':
                bin2dec()
            elif wybor == 'd':
                dec2other()
        else:
            print("Zły wybór... ")
            
        koniec = input("Chcesz kontynuować? (t/n) ")
        if koniec in ['t', 'n']:
            if koniec != 't':
                print("Dzięki za współpracę...")
                break

if __name__ == "__main__":
    main()
        
        
        
          
        
        
        
    
    
