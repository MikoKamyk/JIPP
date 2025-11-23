# Zliczanie liczby samogłosek i spółgłosek w zadanym ciągu
# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0
vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”
tekst = "Programowanie Pythona"    
for znak in tekst:
    if znak.isalpha():
# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków
        if znak.lower() in "aeiouyąęó":
            vowels += 1
        else:
            consonants += 1
# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Liczba samogłosek:", vowels)    
print("Liczba spółgłosek:", consonants)