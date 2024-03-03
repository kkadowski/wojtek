''' 
Moduł pomiaru czasu
K>K> 2023
v. 1.0
'''
from time import perf_counter as pc

def measuretime(func):
    def wrapper(*args, **kwargs):
        start = pc()
        result = func(*args, **kwargs)
        end = pc()
        print(f"Czas wykonania funkcji {func.__name__}: {end-start} sekund. ")
        return result
    return wrapper