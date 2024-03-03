''' 
Obsługa plików
tryb w- write, r - read, a - appned, t - text, b - binarny

'''



# wyraz = "Rower2"

# # file = open("plik.txt","w+b")
# # file.write(wyraz)
# # file.close()

# with open('plik.txt', "w+t") as file:
#     for i in wyraz:
#         file.write(i + "\n")
    
# # odczyt

# with open("plik.txt", "r+t") as f:
#     dane = f.read()
#     print(dane)
    

zdania = ['Pierwsze zdanie.', 'Drugie zdanie.', 'Trzecie zdanie.']

with open("zdania.txt", "w+t") as f:
    for zd in zdania:
        f.write(zd + '\n')


# with open("zdania.txt", "r+t") as f:
#     dane = f.read()
    
#     print(dane)

with open("zdania.txt", "r+t") as f:
    dane = f.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].replace("\n",'')
        
    print(dane)
    print(f"Linii w pliku jest: {len(dane)}")
















