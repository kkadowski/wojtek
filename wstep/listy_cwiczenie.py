''' 
Ćwiczenie z list
K>K> 2023-10-11
v. 1.0
'''

import random as rd

# n = int(input("Podaj ile chcesz wygenerować liczb? "))
# p = int(input("Podaj dolny zakres liczb: "))
# k = int(input("Podaj górny zakres liczb: "))

# if p > k:
#     p, k = k, p  # FlipFlop Python like
    
# lista1 = []
# for i in range(n):
#     lista1.append(rd.randint(p,k))
    
# print(lista1)


#list comprehension
# lista2 = [ rd.randint(p,k) for i in range(n) ]

# print(lista2)


# lista_parzystych = [ i if i%2==0 else "*" for i in range(0,100) ]
# print(lista_parzystych)


# owoce = [ "jabłko", "gruszka", "banan", "wiśnia" ]

# for i in owoce:
#     print(i)
    
# for i in range(len(owoce)):
#     print(f"{i} - {owoce[i]}")
    
# for i, v in enumerate(owoce):
#     print(f"{i} - {v}")
    

listaA = [ 1, 2, 3 ]
listaB = [ 'a', 'b', 'c' ]

if len(listaA) != len(listaB):
    print('Uważaj bo listy mają różną długość. Część lementów może zaginąć.')
nowa = list(zip(listaA, listaB))
print(nowa)









    
     














    