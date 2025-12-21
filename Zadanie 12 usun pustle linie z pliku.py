try:
    with open("raw.txt", "r", encoding="utf-8") as plik_wejsciowy:
        with open("clean.txt", "w", encoding="utf-8") as plik_wyjsciowy:
            
            for linia in plik_wejsciowy:
                
                if linia.strip() != "":
                    plik_wyjsciowy.write(linia)

    print("Operacja zakończona. Oczyszczony tekst znajduje się w pliku clean.txt.")

except FileNotFoundError:
    print("Błąd: Nie znaleziono pliku 'raw.txt'. Upewnij się, że plik istnieje.")