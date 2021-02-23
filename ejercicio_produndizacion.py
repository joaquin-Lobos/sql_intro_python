import sqlite3
import csv

def create_schema():
    conn = sqlite3.connect("libreria.db")
    c = conn.cursor()

    c.execute("""
                DROP TABLE IF EXISTS libro;
            """)

    c.execute("""
            CREATE TABLE libro(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] TEXT NOT NULL,
                [author] TEXT NOT NULL,
                [pages] INTEGER
            );
            """)

    conn.commit()
    conn.close()


def fill():
    with open('libreria.csv') as csvfile:
        data = list(csv.reader(csvfile))
        
    cantidad_filas = len(data)

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    for i in range(1,cantidad_filas):
        c.execute("""
                INSERT INTO libro (title, pages, author)
                VALUES (?,?,?);""", data[i])

    conn.commit()
    conn.close()

def fetch(id):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    if id == 0:
        c.execute('SELECT * FROM libro')
        print("aaaaaaa")
        while True:
            row = c.fetchone()
            if row is None:
                break
            print(row)
    
    else:
        c.execute("SELECT * FROM libro WHERE id =?", (id,)).rowcount
        data = c.fetchone()
        if data == None:
            print("ID no Valido")
        else:
            print(data)
            

def search_author(book_title):

    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    c.execute("SELECT author FROM libro WHERE title =?", (book_title,)).rowcount
    data = c.fetchone()

    if data == None:
        return print("Autor no encontrado")
    else:
        return print("Autor del Libro:", data)

if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch(0)  # Ver todo el contenido de la DB
  # fetch(3)  # Ver la fila 3
  # fetch(20)  # Ver la fila 20

  # Buscar autor
  search_author('Relato de un naufrago')