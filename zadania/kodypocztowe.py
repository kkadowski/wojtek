'''
Napisz aplikację konsolową generującą kody pocztowe
z zakresy podanych dwóch przykładowych kodów

K>K> 2023

89-600 .... 89-620

'''

def kody(kod1, kod2):
    listakodow = [ str(x)[:2]+"-"+str(x)[2:] for x in range(int(kod1.replace("-","")), int(kod2.replace("-",""))+1) ] 
    print(f'Kody: \n {listakodow}')

def main():
    
    kod1 = input("Podaj kod pierwszy: ")
    kod2 = input("Podaj kod ostatni: ")
    kody(kod1, kod2)

if __name__ == "__main__":
    main()

