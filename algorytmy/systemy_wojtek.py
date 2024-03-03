'''
Zamiana Systemów Liczbowych
06-12-2023 Wojtek
v1.0
bin, dec, oct, hex
'''





hex = ['A','B','C','D','E','F']


def bin2dec():
    print("\nbin2dec\n")
    liczba_bin = input("Podaj liczbę binarną: ")
    liczba_bin = liczba_bin[::-1]                   
    l = len(liczba_bin)
    liczba_dec = 0
    for i in range(l):
        liczba_dec += (int(liczba_bin[i]) * (2**i))
        print(f"{i}: liczba{liczba_bin} : {liczba_dec}")
    print(liczba_dec)


def dec2other(podstawa = -1, any = True, liczba_dec = 0):
    if any:
        liczba_dec = input("Podaj liczbę dziesiątkową: ")
    if podstawa == -1:
        podstawa = int(input("podaj podstawę systemu: "))
    if int(liczba_dec) != 0:
        l = int(liczba_dec)
        reszta = 0
        liczba = ''
        while l != 0:
            reszta = l % podstawa
            if reszta > 9:
                liczba += str(hex[reszta-10])
            else:
                liczba += str(reszta)
            l //= podstawa
        liczba = liczba[::-1]
    if any:
        return f"Liczba {liczba_dec} o podstawie 10 w systemie o podstawie {podstawa} to {liczba}."
    else:
        return liczba

def other2dec(podstawa = -1 ,any = True ,liczba_other = 0):
    if any:
        liczba_other = input("Podaj liczbę: ")
    if podstawa == -1:
        podstawa = int(input("Podaj podstawę systemu: "))
    liczba_other = liczba_other[::-1]
    liczba_dec = 0
    for i in range(len(liczba_other)):
        if liczba_other[i].isdigit() :
            liczba_dec += (int(liczba_other[i]) * (podstawa**i))
        else:
            # print(liczba_other[i]
            liczba_dec += hex.index(liczba_other[i]) + 10
    if any:
        return f"Liczba {liczba_other} o podstawie {podstawa} w systemie o podstawie 10 to {liczba_dec}."
    else:
        return liczba_dec

def any2other():
    podstawy = [2,8,10,16]
    value = input("Podaj Liczbę: ")
    while True:
        podstawa = int(input("Podaj podstawę systemu (2,8,10,16): "))
        if podstawa in podstawy:
            break
        else:
            print("Nieobsługiwana Podstawa")
    dec = other2dec(podstawa, False, value)
    rest = podstawy
    rest.remove(podstawa)
    for x in rest:
        print(f"Liczba {value} o podstawie {podstawa} w systemie o podstawie {x} to {dec2other(x, False, dec)}.")




def wstep():
    print("="*50)
    print("Translacja na systemy liczbowe.")
    print("="*50)
    print("Witamy!")

def menu():
    print('''
        MENU:
          b - dowolny do dec
          d - dec do dowolnej
          x - any to rest
          ''')

#============================MAIN==============================

def main():
    wybor = ''
    wstep()

    while True:
        menu()
        
        wybor = input("Wybierz co chcesz zrobić: ")
        if wybor in ['b', 'd','x']:
            if wybor == 'b':
                print(f"{other2dec()}")
            elif wybor == 'd':
                print(dec2other())
            elif wybor == 'x':
                any2other()
        else:
            print("Zły wybór...")
        
        koniec = input("Chcesz Kontynuować? (t/n)")
        if koniec in ['t', 'n']:
            if koniec != 't':
                print("Dzięki za współpracę!")
                break



    
if "__main__" == __name__:
    main()