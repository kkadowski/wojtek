class Osoba:
    def __init__(self, imie, nazwisko, wiek): #konstruktor - metoda inicjująca instancję obiektu
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        
    def przedstaw_sie(self):
        print(f"Nazywam się: {self.imie} {self.nazwisko} i mam {self.wiek} lat.")
        
    
    def zmien_wiek(self, ile):
        self.wiek += ile
        return self.wiek
    
# klasa potomna dziedzicząca z Osoba

class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa = klasa
        
    def przedstaw_sie(self):
        print(f"Jestem uczniem: {self.imie} {self.nazwisko} z klasy {self.klasa} (wiek: {self.wiek})")
        
    def zmien_klase(self, klasa):
        self.klasa = klasa
        return self.klasa
    
    def zmien_wiek(self, ile = 2):
        self.wiek += ile
        return self.wiek
    
class Nauczyciel(Osoba):
    def __init__(self, imie, nazwisko, wiek, przedmiot):
        super().__init__(imie, nazwisko, wiek)
        self.przedmiot = przedmiot
        
    def przedstaw_sie(self):
        print(f"Jestem belfrem {self.imie} {self.nazwisko} i uczę przedmiotu: {self.przedmiot}")
        

osoba1 = Osoba("Jan", "Kowalski", 23)
osoba2 = Uczen("Adam", "Nowak", 13, "2A")
osoba3 = Nauczyciel("Zenon", "Miły", 44, "Chemia")

osoba1.przedstaw_sie()
osoba2.przedstaw_sie()
osoba3.przedstaw_sie()
# osoba2.zmien_wiek(3)
# osoba2.przedstaw_sie()
# osoba2.zmien_klase("3")
# osoba2.przedstaw_sie()
# osoba3.przedstaw_sie()

# print(help(Uczen))
# print(isinstance(osoba2, Osoba))
# print(isinstance(osoba2, Uczen))
# print(isinstance(osoba2, Nauczyciel))

# print(issubclass(Uczen, Osoba))
# print(issubclass(Nauczyciel, Osoba))
# print(issubclass(Uczen, Nauczyciel))

# print(osoba2.__class__.__name__)

print(getattr(osoba2, "imie"))

try:
    print(getattr(osoba2, "przedmiot"))
except Exception as e:
    print(f"Instancja nie ma takiej właściwości")


print(hasattr(osoba2, "imie"))
print(hasattr(osoba2, "przedmiot"))

setattr(osoba3, "imie", "Roman")

osoba3.przedstaw_sie()
