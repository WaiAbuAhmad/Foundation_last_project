import sqlite3
import click




def get_database(statement):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute(statement)
    rows = cur.fetchall()  
    print(rows)   
    return rows 





def insert_database(statement):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()
    conn.close()





