
import random
# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci

questions = ["Why is the sky blue?\n","Why is the sun round?\n","Where are all the dinosaurs?\n"]
answer = ""
# Wybierz losowe pytanie z danej listy za pomocą instrukcji warunkowej
while answer != "to wszystko":
    question = random.choice(questions)
# Zadaj wybrane pytanie za pomocą funkcji input()
# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuje wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje

    answer = input(question).strip().lower()

# Poczekaj do czasu, aż użytkownik wprowadzi hasło „To wszystko”

# Wyświetl wiadomość

print("Gituwa, brak pytan")