'''
Bubblesort
K>K> 2023 
'''
from measuertime import measuretime as mt
import random as rd

@mt
def bubblesort(liczby):
    for i in range(len(liczby)):
        for j in range(len(liczby) -1):
            if liczby[j] > liczby[j+1]:
                #liczby[j], liczby[j+1] = liczby[j+1], liczby[j] # python like
                temp = liczby[j]
                liczby[j] = liczby[j+1]
                liczby[j+1] = temp
    return liczby



liczby = [ rd.randint(1,100) for i in range(1000)]
print(f"Przed sortowaniem: {liczby}")
liczby_po = bubblesort(liczby)
print(f"Po posortowaniu: {liczby_po}")