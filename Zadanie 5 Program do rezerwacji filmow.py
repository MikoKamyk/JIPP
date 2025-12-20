# Utwórz słownik filmów
# klucz: tytuł filmu
# wartość: [kryterium wiekowe, liczba dostępnych biletów]
movies = {
    "Finding Nemo": [5, 2],
    "Moana": [6, 3],
    "Batman": [18, 5],
    "The Lion King": [10, 4]
}

# Pętla działająca w nieskończoność
while True:
    # Pobierz tytuł filmu od użytkownika
    movie = input("Podaj tytuł filmu (lub 'exit' aby zakończyć): ").strip().title()

    # Warunek wyjścia z programu
    if movie.lower() == "exit":
        print("Koniec programu")
        break

    # Sprawdź, czy film istnieje w słowniku
    if movie in movies:
        # Zapytaj użytkownika o wiek
        age = int(input("Podaj swój wiek: "))

        # Pobierz kryterium wiekowe i liczbę biletów
        min_age = movies[movie][0]
        tickets = movies[movie][1]

        # Sprawdź kwalifikowalność wiekową
        if age >= min_age:
            # Sprawdź dostępność miejsc
            if tickets > 0:
                movies[movie][1] -= 1
                print("Rezerwacja udana!")
                print("Pozostałe bilety:", movies[movie][1])
            else:
                print("Brak dostępnych biletów")
        else:
            print("Nie spełniasz kryterium wiekowego")
    else:
        print("Nie ma takiego filmu w repertuarze")