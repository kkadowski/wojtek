'''
Insertsort
K>K> 2023 
'''
from measuertime import measuretime as mt
import random as rd

@mt
def insertsort(liczby):
    for i in range(1, len(liczby)):
        j = i
        while liczby[j] < liczby[j-1] and j > 0:
            liczby[j], liczby[j-1] = liczby[j-1], liczby[j]
            j -= 1
    return liczby



liczby = [ rd.randint(1,100) for i in range(1000) ]
print(f"Przed sortowaniem: {liczby}")
liczby_po = insertsort(liczby)
print(f"Po posortowaniu: {liczby_po}")