''' 
Dekoratory 
'''
from measuertime import measuretime

@measuretime
def iloczyn(liczby):
    il = 1
    for i in liczby:
        il *= i
    return il

# ----------------- MAIN ---------------------
def main():
    n = int(input("Podaj ilość liczb: "))
    liczby = [ int(input(f"Podaj liczbę nr {i+1}:")) for i in range(n) ]
    il = iloczyn(liczby)
    print(f"Iloczyn liczb wynosi {il}")

if __name__ == "__main__":
    main()
    
