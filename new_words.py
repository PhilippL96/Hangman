import sqlite3

def add_word(word: str):
    connection = sqlite3.connect("database.db")
    cur = connection.cursor()
    wordlist = cur.execute("Select word from words").fetchall()
    for element in wordlist:
        if element[0] == word:
            return "IN"
    data = [word, len(word)]
    cur.execute("INSERT INTO words VALUES(?,?)", data)
    connection.commit()
    connection.close()


