'''
Ciąg Fibonacciego
2023 K>K>
'''

def fib(n):
   if n <= 0:
       return []
   elif n == 1:
       return [0]
   elif n == 2:
       return [0,1]
   else:
        fibs = fib(n-1)
        fibs.append(fib(n-1) + fib(n-2))
        return fibs

def fib2(n):
    if n <= 2:
        return 1
    elif n < 3:
        return 1
    return fib2(n-1) + fib2(n-2)




n = int(input("Podaj liczbę całkowitą: "))
nums = fib(n)
numsF = fib2(n)
print(f"Liczby Fibonacciego: {nums}")
print(f"Liczba Fibonacciego: {numsF}")
