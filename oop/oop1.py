'''
OOP      obiekty 
    |              |   
właściwości     metody
'''

class Osoba:
    def __init__(self, imie, nazwisko, wiek): #konstruktor - metoda inicjująca instancję obiektu
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        
    def przedstaw_sie(self):
        print(f"Nazywam się: {self.imie} {self.nazwisko} i mam {self.wiek} lat.")
        
    
    def zmien_wiek(self, ile = 1):
        self.wiek += ile
        return self.wiek
        

osoba1 = Osoba("Krzysztof", "Kadowski", 54) # inicjacja instancji obiektu
osoba2 = Osoba("Wojtek", "Górzyński", 16)

osoba1.przedstaw_sie()
osoba2.przedstaw_sie()

# osoba2.zmien_wiek(2)
# osoba2.przedstaw_sie()

# osoba1.zmien_wiek()
# osoba1.przedstaw_sie()


# print(osoba1.__dict__)     
# print(Osoba.__doc__)
# print(help(Osoba))   


    