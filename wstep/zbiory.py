''' 
zbiory - set

'''

# zb1 = { 2,3,5,4,1,6,4,2,3,2,3 }

# print(zb1)

# lista = [3,45,2,2,3,3,2,3,4,2,2,4]

# elementy = list(set(lista))
# print(elementy)

# zb2 = set()
# zb2.add(3)
# print(zb2)

# zb2.add(5)
# zb2.add(7)

# print(zb2)

# # if 9 in zb2:
# #     zb2.remove(9)
# # else:
# #     print("9 nie istnieje w zbiorze")
# # print(zb2)

# zb2.discard(9)
# print(zb2)


A = {1, 2, 3}
B = {3, 4, 5}

wspolna = A.intersection(B)
print(wspolna)

suma = A.union(B)
print(suma)

roznicaAB = A.difference(B)
print(roznicaAB)

roznicaBA = B.difference(A)
print(roznicaBA)
















