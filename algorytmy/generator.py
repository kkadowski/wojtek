''''
generator liczb 5-10 cyfrowych

10000 - 999 999 999 9
'''

from random import randint

try:
    with open("plik.txt", "+at") as file:
        for i in range(1000):
            file.write(str(randint(10000,9999999999))+"\n")
except FileNotFoundError as err:
    print(f"Plik nie istnieje...")

