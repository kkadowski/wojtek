'''
Słownik - dictionary - mutable 
para klucz - wartość
'''

# osoba = { "imie":"Adam", "wiek": 18, "wzrost": 1.78 }
# print(type(osoba))
# print(osoba)

# print(osoba.keys())
# print(osoba.values())
# print(osoba.items())

# for k, v in osoba.items():
#     print(f"{k} - {v}")


n = int(input("ile chcesz wprowadzić osób: "))
osoby = []

for i in range(n):
    osoba = dict()
    osoba['imie'] = input("Podaj imię: ")
    osoba['wiek'] = int(input("Podaj wiek: "))
    osoba['wzrost'] = float(input("Podaj wzrost w metrach: "))
    osoby.append(osoba)


print(osoby)

#jak wyświetlić imiona

for osoba in osoby:
    print(osoba['imie'])













