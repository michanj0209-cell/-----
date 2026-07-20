class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}")

    def get_info(self):
        return f"Подія: {self.title} ({self.date})"


class Training(Event):
    def __init__(self, title, date, coach):
        super().__init__(title, date)
        self.coach = coach

    def show(self):
        print(f"Тренування: {self.title}, Дата: {self.date}, Тренер: {self.coach}")

    def get_info(self):
        return f"Тренування: {self.title} з тренером {self.coach} на дату {self.date}"


class Birthday(Event):
    def __init__(self, title, date, age):
        super().__init__(title, date)
        self.age = age

    def show(self):
        print(f"День народження: {self.title}, Дата: {self.date}, Виповнюється років: {self.age}")

    def get_info(self):
        return f"День народження: {self.title} ({self.age} років), дата: {self.date}"


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link

    def show(self):
        print(f"Онлайн-подія: {self.title}, Дата: {self.date}, Посилання: {self.link}")


if __name__ == "__main__":
    events = [
        Training("Python OOP", "21.07.2026", "Олександр"),
        Birthday("Олексій", "25.08.2026", 25),
        OnlineEvent("Вебінар", "26.07.2026", "https://zoom.us"),
        Training("Data Science", "01.09.2026", "Марія")
    ]

    for event in events:
        event.show()

    print()

    for event in events:
        if hasattr(event, "get_info"):
            info_string = event.get_info()
            print(info_string)
