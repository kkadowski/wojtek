''' 
Ćwiczenie z list
K>K> 2023-10-11
v. 1.0
'''

n = int(input("Podaj ile elementów chesz dodać do listy: "))
lista = []

for i in range(n):
    lista.append(int(input(f"Podaj element {i+1}: ")))
    
print(lista)

# index, element, kwadrat elementu
for i in range(len(lista)):
    print(f"ELement o indeksie {i} to {lista[i]} a kwadrat to {lista[i]**2}")
    

    
