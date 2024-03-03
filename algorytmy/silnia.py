''' 
Silnia z liczby - n!

K>K> 2023
'''

def silnia(x):
    if x > 1:
        return x * silnia(x-1)
    else:
        return 1
   
def silnia2(x): 
    if x <= 1:
        return 1
    else:
        return x * silnia2(x-1)

n = int(input("Podaj liczbę: "))
print(f"Silnia z {n} wynosi {silnia(n)}.")
print(f"Silnia z {n} wynosi {silnia2(n)}.")

for i in range(n):
    print(f"Silnia z {i} wynosi {silnia(i)}")


    
    