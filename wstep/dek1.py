''' 
Moduł pomiaru czasu
'''
import time

def measuretime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania funkcji {func.__name__}: {end-start} sekund. ")
    return wrapper



@measuretime
def f1():
    for i in range(100000):
        print(f"Numer: {i}")
    return i



def main():
    f1()

if __name__ == "__main__":
    main()
    


