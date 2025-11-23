# Zapytaj użytkownika o nazwisko
name = input("What is your name?: ")

# Zapytaj użytkownika o wiek
age = input("Jaki jest twoj wiek?: ")

# Zapytaj użytkownika o miasto
city = input("Gdzie mieszkasz?: ")

# Zapytaj użytkownika o jego zainteresowania
interest = input("Czym sie interesujesz?: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów
string = "Hi {}, you are {} years old. You live in {} and you love {}!"

output = string.format(name, age, city, interest)

# Wydrukuj tekst wyjściowy
print(output)