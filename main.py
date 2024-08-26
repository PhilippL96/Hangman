from game import game
from get_words import get_word
from new_words import add_word

while True:
    decision = input('Gib "1" ein, um Hangman zu spielen.\nGib "2" ein, um ein neues Wort für die Datenbank hinzuzufügen.\nGib "Q" ein, um das Programm zu verlassen.\n')
    if decision.lower() == "q":
        print("Auf Wiedersehen!")
        break
    elif decision == "1":
        print("Willkommen zum Hangman-Spiel!")
        next_game = True
        while next_game:
            while True:
                try:
                    difficulty = int(input("Welche Schwierigkeitsstufe möchtest du wählen? (1: Leicht, 2: Mittel, 3: Schwer)\n"))
                except ValueError as e:
                    print("Fehler: ", e)
                else:
                    if difficulty < 1 or difficulty > 3:
                        print("Schwierigkeitsstufe muss 1, 2 oder 3 sein!")
                    else:
                        break

            if difficulty == 1:
                max_versuche = 7
            elif difficulty == 2:
                max_versuche = 5
            else:
                max_versuche = 3
            word = get_word(difficulty)
            game(word, max_versuche)
            again = input('Um abzubrechen, "Q" eingeben.\nUm nochmal zu spielen, beliebiges anderes Symbol eingeben.\n')
            if again.lower() == "q":
                next_game = False
    elif decision == "2":
        word = input("Welches Wort möchtest du Zur Datenbank hinzufügen?\n").upper()
        for char in word:
            try:
                assert char.isalpha()
            except AssertionError:
                print("Bitte nur ein Wort eingeben, das nur aus Buchstaben besteht!")
                word = None
                break
        if word:
            test = add_word(word)
            if test:
                print(f"{word} ist bereits vorhanden!")
            else:
                print(f"Erfolgreich Wort {word} hinzugefügt!")

    else:
        print("Ungültige Eingabe! Versuchs nochmal.")