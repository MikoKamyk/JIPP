imie = input("Podaj swoje imię: ")
wiek = input("Podaj swój wiek: ")

with open("user.txt", "w", encoding="utf-8") as plik:
    plik.write(f"Imię: {imie} Wiek: {wiek}")

print("Dane zostały zapisane do pliku user.txt")