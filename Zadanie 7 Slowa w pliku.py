import os

folder_skryptu = os.path.dirname(os.path.abspath(__file__))
sciezka_do_pliku = os.path.join(folder_skryptu, "story.txt")

try:
    with open(sciezka_do_pliku, "r", encoding="utf-8") as plik:
        tekst = plik.read()
        slowa = tekst.split()
        print(f"Liczba słów: {len(slowa)}")
except FileNotFoundError:
    print(f"Nadal nie widzę pliku. Szukałem tutaj: {sciezka_do_pliku}")