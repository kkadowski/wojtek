''' 
Binary search
2023 K>K>
'''

lista = []

def bin_search(lista, s, l, p):
    if l > p:
        return -1
    
    pivot = (l + p) // 2
    if s == lista[pivot]:
        return pivot
    
    if s < lista[pivot]:
        return bin_search(lista, s, l, pivot -1)
    else:
        return bin_search(lista, s, pivot + 1, p)
        

def wprowadzanie():
    while True:
        try:
            n = int(input("Ile liczb chesz wprowadzić do listy: "))
            for i in range(n):
                lista.append(int(input(f"Podaj liczbę do listy {i+1}= ")))
            lista.sort()
            s = int(input("Podaj szukaną wartość w liście: "))
            return (lista, s)
        
        except ValueError:
            print(f"Musi być liczba...")

     

def main():
    lista, s = wprowadzanie()
    print(f"Szukasz liczby {s} w liście {lista}")
    if bin_search(lista, s, 0, len(lista)-1) == -1:
        print(f"W liście nie ma liczby {s}")
    else:
        print(f"Liczba {s} znajduje się na pozycji {(bin_search(lista, s, 0,len(lista)-1)) + 1}")


if __name__ == "__main__":
    main()  