class Konto:
    
    oprocentowanie = 0.10
        
    def __init__(self):
        self.__saldo = 0
        
    def pokaz_saldo(self):
        print(f"Obecne saldo: {self.__saldo}")
        
    def wplata(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
        else:
            print(f"Nie można wpłacić wartości ujemnej {kwota}. Saldo bez mian.")
        return self.__saldo
    
    def wyplata(self, kwota):
        if kwota> 0 and kwota <= self.__saldo:
            self.__saldo -= kwota
        return self.__saldo
    
    def wzrost_salda(self):
        self.__saldo *= 1 + self.oprocentowanie
        return self.__saldo
    
    
s1 = Konto()
s2 = Konto()
   
s1.pokaz_saldo()
s1.wplata(100)
s1.pokaz_saldo()
s1.wyplata(60)
s1.pokaz_saldo()
s1.wzrost_salda()
s1.pokaz_saldo()
 
s2.pokaz_saldo()
s2.wplata(200)
s2.pokaz_saldo()

    
    
