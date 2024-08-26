import sqlite3
import random



def get_word(difficulty: int) -> str:
    connection = sqlite3.connect("database.db")
    cur = connection.cursor()
    if difficulty == 1:
        word_list = cur.execute("Select word from words where letters < 5").fetchall()
    elif difficulty == 2:
        word_list = cur.execute("Select word from words where letters > 4 and letters < 7").fetchall()
    else:
        word_list = cur.execute("Select word from words where letters > 6").fetchall()
    
    return random.choice(word_list)[0]

