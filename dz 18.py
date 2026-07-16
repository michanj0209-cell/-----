class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Курс: {self.course}")
        print("-" * 25)

    def change_course(self, new_course):
        self.course = new_course


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def show_info(self):
        status = "Виконано" if self.completed else "Не виконано"
        print(f"Завдання: {self.title} | Status: {status}")


class Event:
    def __init__(self, title, date, description=""):
        self.title = title
        self.date = date
        self.description = description

    def show(self):
        print(f"Подія: {self.title}")
        print(f"Дата: {self.date}")
        status_desc = self.description if self.description else "Немає опису"
        print(f"Опис: {status_desc}")
        print("-" * 30)

    def update_description(self, new_description):
        self.description = new_description


print("=== ДЕМОНСТРАЦІЯ КЛАСУ STUDENT ===")
student1 = Student("Олександр", 19, 2)
student2 = Student("Марія", 20, 3)

student1.show_info()
student2.show_info()

print("=== ДЕМОНСТРАЦІЯ КЛАСУ TASK ===")
task = Task("Зробити домашнє завдання з ООП")
task.show_info()

print("=== ДЕМОНСТРАЦІЯ КЛАСУ EVENT ===")
event = Event("Модульний контроль", "20.10.2026")
event.show()


