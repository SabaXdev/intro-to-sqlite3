import sqlite3
import random

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS book (
          title text,
          pages integer,
          cover_type text,
          category text 
          )""")


def random_books(num_books):
    res_books = []
    for book_id in range(num_books):
        title = "Book " + str(book_id)
        pages = random.randint(80, 800)
        cover_type = random.choice(['Hardcover', 'Paperback'])
        category = random.choice(['Classics', 'Fantasy', 'Humor', 'Mystery', 'Adventure', 'Romance'])
        res_books.append((title, pages, cover_type, category))
    return res_books


books = random_books(10)

c.executemany("INSERT INTO book (title, pages, cover_type, category) VALUES (?, ?, ?, ?)", books)

c.execute("SELECT AVG(pages) FROM book")
avg_pages = c.fetchone()[0]
print("Average number of pages is: ", avg_pages)

c.execute("SELECT title FROM book WHERE pages = (SELECT MAX(pages) FROM book)")
book_with_most_pages = c.fetchone()[0]
print("Title of the book with most pages is: ", book_with_most_pages)

conn.commit()
conn.close()
