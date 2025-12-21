import os

folder_skryptu = os.path.dirname(os.path.abspath(__file__))
sciezka_do_pliku = os.path.join(folder_skryptu, "numbers.txt")

suma = 0

try:
    with open("numbers.txt", "r") as plik:
        for linia in plik:
            liczba = int(linia.strip())
            
            suma += liczba

    print(f"Suma liczb: {suma}")

except FileNotFoundError:
    print("Błąd: Plik 'numbers.txt' nie istnieje.")
except ValueError:
    print("Błąd: Jedna z linii w pliku nie jest poprawną liczbą.")