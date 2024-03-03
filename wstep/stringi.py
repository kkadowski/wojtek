''' 
Stringi - immutale
'''

# t1 = "Jakiś tekst"
# t2 = 'Inne zdanie'
# t3 = ''' 
#     Wiele zdań
#     w kilku
#     linijkach
# '''

# print(type(t1))
# print(type(t2))
# print(type(t3))

# zdanie = "John's mother"
# print(zdanie)

# zdanie = "Nazywam sie Krzysztof i uczę programowania."
# adres = "Mieszkam w Chojnicach."

# dane = zdanie +" "+ adres
# print(dane)

# print(f"Dłuchość danych to: {len(dane)}")



# for litera in dane:
#     if litera.isupper() == True:
#         print(litera)
        
# print(dane.capitalize())
# print(dane.endswith('ne.'))  
# print(dane.find('i'))  
# print(dane[3].isalpha())  
# print(dane[3].isdigit())  

# pusty = ''
# print(pusty.join(dane))

# print(''.join(dane[2]))

# print(dane.replace('i','X'))

dane= " jakieś zdanie. inne zdanie. "

wyrazy = dane.split()
for i in range(len(wyrazy)):
    if wyrazy[i].endswith('.'):
        wyrazy[i] = wyrazy[i].replace(".","")
print(wyrazy)

wyr = dane.strip()
print(wyr)

innedane = 'imie:nazwisko:wiek:plec'

inne = innedane.split(":")
print(inne)




        


