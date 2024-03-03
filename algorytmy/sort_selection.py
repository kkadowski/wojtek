'''
Selectionsort
K>K> 2023 
'''
from measuertime import measuretime as mt
import random as rd

@mt
def insertsort(liczby):
    for i in range(len(liczby)):
        min = i
        for j in range(i, len(liczby)):
            if liczby[min] > liczby[j]:
                min = j
        liczby[i], liczby[min] = liczby[min], liczby[i]
    return liczby



liczby = [ rd.randint(1,100) for i in range(1000) ]
print(f"Przed sortowaniem: {liczby}")
liczby_po = insertsort(liczby)
print(f"Po posortowaniu: {liczby_po}")