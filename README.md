# Hangman-Spiel

Dies ist eine einfache Version eines Hangman-Spiels, das als Teil eines vorgegebenen Projekts in meiner Weiterbildung entwickelt wurde. Das Projekt umfasst mehrere Python-Skripte, die zusammen ein vollständiges Hangman-Spiel ermöglichen.

## Skripte

- **`get_words.py`**: Enthält eine Funktion, die ein Wort einer bestimmten Länge (abhängig vom Parameter `difficulty`) zufällig aus der Datenbank `database.db` auswählt und zurückgibt. Diese Funktion wird verwendet, um ein zufälliges Wort für das Hangman-Spiel zu generieren.

- **`new_words.py`**: Beinhaltet eine Funktion, die ein Wort entgegennimmt und es in der Datenbank speichert. Diese Funktion wird in `main.py` verwendet, um es dem Benutzer zu ermöglichen, ein selbst ausgewähltes Wort in die Datenbank hinzuzufügen, das dann später zufällig für das Spiel ausgewählt werden kann.

- **`game.py`**: Implementiert die Logik des Hangman-Spiels als Funktion. Es ermöglicht dem Spieler, Buchstaben zu raten, bis alle Buchstaben des Wortes erraten wurden oder der Spieler verliert.

- **`main.py`**: Führt das Hauptprogramm aus. Es startet eine Schleife, die entweder das Spiel startet oder es dem Benutzer ermöglicht, ein neues Wort hinzuzufügen, bis der Spieler das Programm beendet.

## Verwendung

1. **Datenbank einrichten**: Stelle sicher, dass `database.db` im Projektverzeichnis vorhanden ist.

2. **Neues Wort hinzufügen**: Um ein neues Wort zur Datenbank hinzuzufügen, führe `main.py` aus und wähle die Option, ein neues Wort hinzuzufügen.

3. **Spiel spielen**: Um das Hangman-Spiel zu spielen, führe `main.py` aus und wähle die Option, das Spiel zu starten.

## Installation

Stelle sicher, dass Python installiert ist. Die genutzten Bibliotheken sind Teil der Python-Standardbibliothek.