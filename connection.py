import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('project.db')
        print("Connected to the database")
        return conn
    except sqlite3.Error as e:
        print(e)
    return None