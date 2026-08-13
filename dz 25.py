import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    description TEXT
)
""")
conn.commit()

while True:
    print("\nВиберіть дію:")
    print("1. Додати книгу")
    print("2. Видалити книгу за ID")
    print("3. Показати всі книги списком")
    print("4. Показати загальну кількість книг")
    print("5. Вийти")
    
    choice = input("Введіть номер дії: ")
    
    if choice == "1":
        title = input("Введіть назву книги: ")
        author = input("Введіть автора: ")
        
        while True:
            year_input = input("Введіть рік випуску: ")
            try:
                year = int(year_input)
                break
            except ValueError:
                print("Помилка: Рік має бути числовим значенням! Спробуйте ще раз.")
                
        description = input("Введіть опис книги: ")
        
        cursor.execute(
            "INSERT INTO books (title, author, year, description) VALUES (?, ?, ?, ?)",
            (title, author, year, description)
        )
        conn.commit()
        print(f"Книгу '{title}' успешно добавлено до бази даних.")
        
    elif choice == "2":
        book_id = input("Введіть ID книги для видалення: ")
        
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        print(f"Запит на видалення книги з ID {book_id} виконано.")
        
    elif choice == "3":
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        print("Книги в базі даних:")
        if not books:
            print("База даних порожня.")
        else:
            for book in books:
                print(f"ID: {book[0]}, Назва: {book[1]}, Автор: {book[2]}, Рік: {book[3]}, Опис: {book[4]}")
                
    elif choice == "4":
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        print(f"Загальна кількість книг у базі даних: {count}")
        
    elif choice == "5":
        print("Вихід з програми. До побачення!")
        break
        
    else:
        print("Невірний вибір. Будь ласка, виберіть від 1 до 5.")

conn.close()
