# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd! Dzielenie przez zero."

# Wyświetl listę operacji
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Pozwól użytkownikowi wybrać żądane działanie na podstawie wyświetlonej listy poleceń
op = input("Please enter choice (a/ b/ c/ d): ")

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowitych
num1 = int(input("Wprowadź pierwszą liczbę: "))
num2 = int(input("Wprowadź drugą liczbę: "))

# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.
if op == 'a':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif op == 'b':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif op == 'c':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif op == 'd':
    print(f"{num1} / {num2} = {divide(num1, num2)}")

# Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie
else:
    print("Nieprawidłowy wybór! Wybierz a, b, c lub d.")