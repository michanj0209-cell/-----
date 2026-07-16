import json

FILENAME = "library.json"

def load_library():
    """
    Автоматичне завантаження даних при запуску програми (Пункт 7).
    Якщо файл відсутній, обробляється FileNotFoundError та створюється порожній словник.
    """
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # Суворо за ТЗ: якщо файл відсутній, створюється порожній словник
        return {}
    except json.JSONDecodeError:
        print("Помилка: Файл JSON пошкоджено. Створено порожню бібліотеку.")
        return {}
    except IOError:
        print("Помилка при відкритті файлу. Створено порожню бібліотеку.")
        return {}

def save_library(library):
    """6. Збереження даних у файл library.json."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(library, file, ensure_ascii=False, indent=4)
    except IOError:
        print("Помилка при збереженні даних у файл!")

def add_book(library):
    """2. Додавання книги."""
    print("\n--- Додавання книги ---")
    title = input("Назва книги: ").strip()
    author = input("Автор: ").strip()
    
    # Пункт 7: перевірка правильності введення року видання
    while True:
        try:
            year_input = input("Рік видання: ").strip()
            year = int(year_input)  # Викличе ValueError, якщо введено не число
            break
        except ValueError:
            print("Помилка: Рік видання повинен бути цілим числом! Спробуйте ще раз.")
            
    genre = input("Жанр: ").strip()
    
    # Генерація унікального ID
    if library:
        next_id = max(int(k) for k in library.keys()) + 1
    else:
        next_id = 1
        
    str_id = str(next_id)
    
    library[str_id] = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    
    save_library(library)
    print("Книгу успішно додано.")

def view_all_books(library):
    """3. Перегляд усіх книг."""
    print("\n--- Перегляд усіх книг ---")
    if not library:
        print("Бібліотека порожня")
        return
        
    for book_id, info in library.items():
        print(f"\nID: {book_id}")
        print(f"Назва: {info['title']}")
        print(f"Автор: {info['author']}")
        print(f"Рік видання: {info['year']}")
        print(f"Жанр: {info['genre']}")

def delete_book(library):
    """4. Видалення книги за ID."""
    print("\n--- Видалення книги ---")
    book_id_input = input("Введіть ID книги для видалення: ").strip()
    
    # Пункт 7: перевірка введеного ID
    try:
        # Перевіряємо, чи є введене значення числом
        int(book_id_input) 
        
        if book_id_input in library:
            del library[book_id_input]
            save_library(library)
            print(f"Книгу з ID {book_id_input} успішно видалено.")
        else:
            print("Книгу не знайдено")
            
    except ValueError:
        print("Помилка: ID книги має бути числовим значенням!")
    except Exception as e:
        print(f"Виникла інша помилка при видаленні: {e}")

def find_books_by_author(library):
    """5. Пошук книг за автором."""
    print("\n--- Пошук книг за автором ---")
    search_author = input("Введіть ім'я автора: ").strip().lower()
    found = False
    
    for book_id, info in library.items():
        if search_author in info['author'].lower():
            print(f"\nID: {book_id}")
            print(f"Назва: {info['title']}")
            print(f"Рік видання: {info['year']}")
            print(f"Жанр: {info['genre']}")
            found = True
            
    if not found:
        print("Книг цього автора не знайдено")

def main():
    library = load_library()
    
    while True:
        print("\n--- Бібліотека книг ---")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Видалити книгу")
        print("4. Знайти книгу за автором")
        print("5. Вийти")
        
        choice = input("Виберіть пункт меню (1-5): ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_all_books(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "4":
            find_books_by_author(library)
        elif choice == "5":
            print("Дякуємо за використання програми. До побачення!")
            break
        else:
            print("Некоректний вибір! Будь ласка, введіть число від 1 до 5.")

if __name__ == "__main__":
    main()
