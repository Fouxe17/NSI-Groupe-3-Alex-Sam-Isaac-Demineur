import sqlite3
import pathlib

current_path = pathlib.Path.cwd()
save_path = current_path / "src" / "data" / "Sauvegarde.db"

def open_database():
    conn = sqlite3.connect(save_path)
    cursor = conn.cursor()
    return conn, cursor

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
# get_rows()
