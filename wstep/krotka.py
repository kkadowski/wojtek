''' 
krotki - tuple - immutable
'''

kr1 = (2,3,5,6)

print(kr1)

kr1 = kr1 + (4,)

print(kr1)


lista = list(kr1)
lista.append(4)
kr1 = tuple(lista)
print(kr1)

for i in kr1:
    print(i)
    
for i, v in enumerate(kr1):
    print(f"{i} - {v}")
    
    
