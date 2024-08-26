def game(word: str, max_versuche: int) -> None:
    hangman_image = """
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    """
    erraten = []
    versuche = 0
    while True:
        ausgabe = "".join("_ " if char not in erraten else char + " " for char in word)
        print(ausgabe)
        if not "_" in ausgabe:
            print("Du hast gewonnen!")
            break
        if versuche == max_versuche:
            print("Leider verloren.")
            print(hangman_image)
            print("Richtige Antwort:")
            print("".join(char + " " for char in word))
            break
        print(f"Du hast noch {max_versuche - versuche} Versuche.")
        guess = input("Welchen Buchstaben rätst du? ").upper()
        try:
            assert guess.isalpha()
        except AssertionError:
            print("Ungültige Eingabe.")
            versuche += 1
            continue

        if guess in erraten:
            print("Buchstabe bereits erraten.")
            continue

        elif guess in word:
            print("Glückwunsch! Richtig geraten!")
            erraten.append(guess)

        else:
            print("Leider nicht richtig.")
            versuche += 1
