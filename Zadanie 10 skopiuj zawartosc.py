try:
    with open("numbers.txt", "r", encoding="utf-8") as plik_zrodlowy:
        zawartosc = plik_zrodlowy.read()

    with open("copy.txt", "w", encoding="utf-8") as plik_docelowy:
        plik_docelowy.write(zawartosc)

    print("Kopiowanie zakończone sukcesem! Utworzono plik copy.txt.")

except FileNotFoundError:
    print("Błąd: Plik źródłowy 'numbers.txt' nie istnieje.")