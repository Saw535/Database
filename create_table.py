from faker import Faker
import connection

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            group_id INTEGER NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Groups (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            teacher_name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grades (
            id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            subject_name TEXT NOT NULL,
            teacher_name TEXT NOT NULL,
            grade INTEGER NOT NULL,
            date TEXT NOT NULL
        );
    ''')

    conn.commit()
    print("Tables created successfully")

def insert_fake_data(conn):
    fake = Faker()
    cursor = conn.cursor()

    for i in range(1, 4):
        cursor.execute("INSERT INTO Groups (name) VALUES (?)", (f"Group-{i}",))
    
    for i in range(1, 6):
        cursor.execute("INSERT INTO Teachers (name) VALUES (?)", (fake.name(),))

    for i in range(1, 9):
        teacher_name = cursor.execute("SELECT name FROM Teachers ORDER BY RANDOM() LIMIT 1;").fetchone()[0]
        cursor.execute("INSERT INTO Subjects (name, teacher_name) VALUES (?, ?)",
                       (f"Subject-{i}", teacher_name))

    for i in range(1, 51):
        student_name = fake.name()
        group_id = i % 3 + 1
        cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (student_name, group_id))
        for j in range(1, 9):
            subject_name = f"Subject-{j}"
            teacher_name = cursor.execute("SELECT teacher_name FROM Subjects WHERE name=?", (subject_name,)).fetchone()[0]
            cursor.execute("INSERT INTO Grades (student_name, subject_name, teacher_name, grade, date) VALUES (?, ?, ?, ?, ?)",
                           (student_name, subject_name, teacher_name, fake.random_int(min=1, max=12), fake.date_this_year()))

    conn.commit()
    print("Fake data inserted successfully")

def main():
    conn = connection.create_connection()
    if conn is None:
        return

    create_tables(conn)

    insert_fake_data(conn)

    conn.close()

if __name__ == "__main__":
    main()