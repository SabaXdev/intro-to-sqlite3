Random Book Generator

This Python script generates a SQLite database example.db containing randomly generated book entries. Each book entry consists of a title, number of pages, cover type, and category. The script then calculates and displays the average number of pages of all books in the database and identifies the book with the highest number of pages.
Prerequisites

Before running the script, ensure you have the following installed:

    Python 3.x
    SQLite3 library for Python

Usage

    Clone or download the repository to your local machine.
    Navigate to the directory containing the Python script.
    Run the script using the command:

    python script_name.py

Code Explanation

    The script establishes a connection to the SQLite database example.db.
    It creates a table named book if it does not already exist, with columns for title, pages, cover_type, and category.
    A function random_books(num_books) generates random book entries with specified attributes (title, pages, cover type, category).
    The generated books are inserted into the book table using the executemany() method.
    The script calculates the average number of pages of all books and identifies the book with the most pages using SQL queries.
    Results are displayed in the console.

Example Output

csharp

Average number of pages is:  414.1
Title of the book with most pages is:  Book 7

License

This project is licensed under the MIT License - see the LICENSE file for details.
