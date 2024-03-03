
a = 8

try:
    print(a/b)
except ZeroDivisionError:
    print("Nie dziele przez zero")
except Exception as e:
    print(f"Nieoczekiwany błąd: '{e}'")