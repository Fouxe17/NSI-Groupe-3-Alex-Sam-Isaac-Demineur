import sqlite3

def open_database():
    conn = sqlite3.connect("Jeu/src/data/Sauvegarde.db")
    cursor = conn.cursor()
    return conn, cursor

def add_values():
    conn,cursor = open_database()
    cursor.execute(
        """
        ALTER TABLE users
        ADD monsters_killed INT
        """
    )
    conn.close()

def add_killed_monsters(id=1,count=10):
    conn,cursor = open_database()
    cursor.execute(
        """
        UPDATE users SET monsters_killed = monsters_killed + ? WHERE id = ?
        """,
        (count, id)
    )
    conn.commit()
    conn.close()

def set_killed_monsters(id=1,killeds=1) -> None:
    conn,cursor = open_database()
    cursor.execute(
        """
        UPDATE users SET monsters_killed = ? WHERE id = ?
        """,
        (killeds, id)
    )
    conn.commit()
    conn.close()

def set_best_score(id:int,score:int):
    conn,cursor = open_database()
    cursor.execute(
        """
            UPDATE users SET max_score = ? WHERE id = ?
        """,
        (score,id)
    )
    conn.commit()
    # cursor.execute("SELECT * FROM users")
    # l = cursor.fetchall()
    # print(l)
    conn.close()

def get_rows():
    conn,cursor = open_database()
    cursor.execute("SELECT * FROM users")
    l = cursor.fetchall()
    conn.close()
    return l

# set_best_score(1,0)
# add_values()
# add_killed_monsters(1,50)
# set_killed_monsters(1,0)
# l = get_rows()
# print(l)