'''
Szyfr Cezara
'''
ile = 94

def szyfruj():
    tekst = input("Podaj tekst do zaszyfrowania:")
    klucz = int(input("Podaj klucz (liczba): "))
    szyfr = ''
    for litera in tekst:
        szyfr += chr(32 + ((int(ord(litera)) + klucz - 32) % ile))
    print(f"Szyfr to: {szyfr}_ ")

def deszyfruj():
    tekst = input("Podaj tekst do odszyfrowania:")
    klucz = int(input("Podaj klucz (liczba): "))
    szyfr = ''
    for litera in tekst:
        szyfr += chr(32 + ((int(ord(litera)) - klucz - 32) % ile))
    print(f"Tekst jawny to: {szyfr} ")

def menu():
    print("=" * 60)
    print("-"*15, "Szyf Cezara - rozszerzony", "-" * 15)
    print("=" * 60)
    print("MENU: s - szyfrowanie, d- deszyfrowanie")
    odp = input("Wybierz działanie: ")
    return odp


odp = menu()
if odp in ['s', 'd']:
    if odp == 's':
        szyfruj()
    elif odp == 'd':
        deszyfruj()
else:
    print("Zły wybór...")