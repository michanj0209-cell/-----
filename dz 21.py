import datetime
import json
import os


class Book:

    def __init__(
        self, id: int, title: str, author: str, year: int, is_borrowed: bool = False
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def print_info(self) -> None:
        status = "📘 [в бібліотеці]" if not self.is_borrowed else "📙 [видана]"
        print(
            f"ID: {self.id} | «{self.title}» — {self.author} ({self.year} р.) {status}"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_borrowed": self.is_borrowed,
        }


class Library:

    def __init__(self, filename: str = "library.json"):
        self.filename = filename
        self.books = []
        self.load()

    def load(self) -> None:
        if not os.path.exists(self.filename):
            self.books = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            print("⚠️ Помилка читання файлу даних. Створено порожню бібліотеку.")
            self.books = []

    def save(self) -> None:
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(
                    [book.to_dict() for book in self.books],
                    f,
                    ensure_ascii=False,
                    indent=4,
                )
        except IOError:
            print("❌ Не вдалося зберегти дані у файл!")

    def get_next_id(self) -> int:
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def find_book_by_id(self, book_id: int) -> Book | None:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def input_year(self) -> int:
        current_year = datetime.datetime.now().year
        while True:
            try:
                year = int(input("Введіть рік видання (від 1000 до поточного): "))
                if 1000 <= year <= current_year:
                    return year
                print(f"❌ Рік має бути в діапазоні від 1000 до {current_year}!")
            except ValueError:
                print("❌ Помилка! Введіть коректне число.")

    def input_id(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Помилка! ID має бути числом.")

    def add_book(self) -> None:
        title = input("Введіть назву книги: ").strip()
        author = input("Введіть автора книги: ").strip()

        if not title or not author:
            print("❌ Назва та автор не можуть бути порожніми!")
            return

        year = self.input_year()
        new_id = self.get_next_id()

        new_book = Book(
            id=new_id, title=title, author=author, year=year, is_borrowed=False
        )
        self.books.append(new_book)
        self.save()
        print(f"✅ Книгу успішно додано! ID: {new_id}")

    def view_all_books(self) -> None:
        if not self.books:
            print("📬 Бібліотека порожня.")
            return

        print("\nВиберіть сортування:")
        print("1 — За назвою")
        print("2 — За автором")
        choice = input("Ваш вибір: ").strip()

        if choice == "2":
            sorted_books = sorted(self.books, key=lambda b: b.author.lower())
        else:
            sorted_books = sorted(self.books, key=lambda b: b.title.lower())

        print("\n--- Список книг ---")
        for book in sorted_books:
            book.print_info()

    def delete_book(self) -> None:
        book_id = self.input_id("Введіть ID книги для видалення: ")
        book = self.find_book_by_id(book_id)

        if book:
            self.books.remove(book)
            self.save()
            print(f"✅ Книгу з ID {book_id} успішно видалено!")
        else:
            print(f"❌ Книгу з ID {book_id} не знайдено.")

    def borrow_book(self) -> None:
        book_id = self.input_id("Введіть ID книги для видачі: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print(f"❌ Книгу з ID {book_id} не знайдено.")
            return

        if book.is_borrowed:
            print("❌ Ця книга вже видана іншому читачеві!")
        else:
            book.is_borrowed = True
            self.save()
            print(f"✅ Книгу успішно видано читачеві!")

    def return_book(self) -> None:
        book_id = self.input_id("Введіть ID книги для повернення: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print(f"❌ Книгу з ID {book_id} не знайдено.")
            return

        if not book.is_borrowed:
            print("📬 Книга вже знаходиться в бібліотеці.")
        else:
            book.is_borrowed = False
            self.save()
            print(f"✅ Книгу успішно повернено до бібліотеки!")

    def find_by_author(self) -> None:
        author_query = input("Введіть ім'я автора для пошуку: ").strip().lower()
        found_books = [
            b for b in self.books if author_query in b.author.lower()
        ]

        if found_books:
            print(f"\n--- Знайдені книги за запитом '{author_query}': ---")
            for book in found_books:
                book.print_info()
        else:
            print("❌ Книг цього автора не знайдено.")

    def find_by_keyword(self) -> None:
        keyword = input("Введіть ключове слово для пошуку в назві: ").strip().lower()
        found_books = [b for b in self.books if keyword in b.title.lower()]

        if found_books:
            print(f"\n--- Знайдені книги за запитом '{keyword}': ---")
            for book in found_books:
                book.print_info()
        else:
            print("❌ Книг із таким ключовим словом не знайдено.")


def main():
    library = Library()

    while True:
        print("\n--- Бібліотека ---")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Видалити книгу")
        print("4. Видати книгу")
        print("5. Повернути книгу")
        print("6. Пошук за автором")
        print("7. Пошук за ключовим словом")
        print("8. Вийти")

        choice = input("Виберіть пункт меню (1-8): ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_all_books()
        elif choice == "3":
            library.delete_book()
        elif choice == "4":
            library.borrow_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            library.find_by_author()
        elif choice == "7":
            library.find_by_keyword()
        elif choice == "8":
            print("До побачення! Програму завершено.")
            break
        else:
            print("❌ Некоректний вибір. Спробуйте ще раз (1-8).")


if __name__ == "__main__":
    main()
