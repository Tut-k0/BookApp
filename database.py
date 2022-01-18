import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Book (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         Title TEXT, 
                                         Author TEXT, 
                                         Year INTEGER, 
                                         ISBN TEXT)
        """
    )
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Book (Title, Author, Year, ISBN)
        VALUES (?, ?, ?, ?)
        """, (title, author, year, isbn)
    )
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Book")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",
                   (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Book WHERE Id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Book SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE Id = ?",
                   (title, author, year, isbn, id,))
    conn.commit()
    conn.close()


connect()
# insert("Extreme Ownership", "Jocko Willink", 2017, "9781250183866")
# insert("12 Rules for Life", "Jordan B. Peterson", 2018, "0345816021")
# insert("Beyond Order", "Jordan B. Peterson", 2021, "0593084640")
# insert("The Hunger Games", "Suzanne Collins", 2010, "9780439023528")
# insert("Point Blank", "Anthony Horowitz", 2006, "9780142406120")
