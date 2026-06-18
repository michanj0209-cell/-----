import json
import os

DATA_FILE = "planner.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        print("Помилка завантаження даних. Створено новий планувальник.")
        return {}

def save_data(planner):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(planner, file, ensure_ascii=False, indent=4)
        print("Дані успішно збережено!")
    except:
        print("Помилка при збереженні даних.")

def add_task(planner):
    print("\n--- Додавання нової події ---")
    
    while True:
        title = input("Введіть назву події: ")
        if title == "":
            print("Помилка: Назва події не може бути порожньою! Спробуйте ще раз.")
        else:
            break

    while True:
        date_str = input("Введіть дату (РРРР-ММ-ДД): ")
        
        if len(date_str) != 10:
            print("Помилка: Некоректна довжина дати! Має бути 10 символів (наприклад, 2026-06-15).")
        elif date_str[4] != "-" or date_str[7] != "-":
            print("Помилка: Дефіси мають бути на своїх місцях (РРРР-ММ-ДД).")
        else:
            year = date_str[0:4]
            month = date_str[5:7]
            day = date_str[8:10]
            
            if year.isdigit() == False or month.isdigit() == False or day.isdigit() == False:
                print("Помилка: Рік, місяць та день мають складатися лише з цифр.")
            else:
                int_month = int(month)
                int_day = int(day)
                
                if int_month < 1 or int_month > 12:
                    print("Помилка: Місяць має бути в діапазоні від 01 до 12.")
                elif int_day < 1 or int_day > 31:
                    print("Помилка: День має бути в діапазоні від 01 до 31.")
                else:
                    break

    while True:
        time_str = input("Введіть час (ГГ:ХХ): ")
        
        if len(time_str) != 5:
            print("Помилка: Некоректна довжина часу! Має бути 5 символів (наприклад, 10:00).")
        elif time_str[2] != ":":
            print("Помилка: Двокрапка має бути на своєму місці (ГГ:ХХ).")
        else:
            hour = time_str[0:2]
            minute = time_str[3:5]
            
            if hour.isdigit() == False or minute.isdigit() == False:
                print("Помилка: Години та хвилини мають складатися лише з цифр.")
            else:
                int_hour = int(hour)
                int_minute = int(minute)
                
                if int_hour < 0 or int_hour > 23:
                    print("Помилка: Години мають бути в діапазоні від 00 до 23.")
                elif int_minute < 0 or int_minute > 59:
                    print("Помилка: Хвилини мають бути в діапазоні від 00 до 59.")
                else:
                    break

    description = input("Введіть опис події (опціонально): ")

    new_id = 1
    while str(new_id) in planner:
        new_id = new_id + 1
    task_id_str = str(new_id)

    planner[task_id_str] = {
        "title": title,
        "date": date_str,
        "time": time_str,
        "description": description
    }
    
    save_data(planner)
    print("Подію успішно додано!")

def view_tasks(planner):
    print("\n--- Список усіх подій ---")
    if len(planner) == 0:
        print("Планувальник порожній. Подій немає.")
    else:
        for task_id in planner:
            task = planner[task_id]
            print("ID:", task_id, "| [", task["date"], task["time"], "]", task["title"])
            if task["description"] != "":
                print("   Опис:", task["description"])
            print("------------------------------")

def delete_task(planner):
    view_tasks(planner)
    if len(planner) == 0:
        return

    task_id = input("\nВведіть ID події для видалення: ")

    if task_id in planner:
        del planner[task_id]
        
        new_planner = {}
        index = 1
        for old_id in planner:
            new_planner[str(index)] = planner[old_id]
            index = index + 1
            
        planner.clear()
        for key in new_planner:
            planner[key] = new_planner[key]
            
        save_data(planner)
        print("Подію успішно видалено.")
    else:
        print("Події з таким ID не знайдено.")

def search_by_date(planner):
    print("\n--- Пошук за датою ---")
    date_str = input("Введіть дату для пошуку (РРРР-ММ-ДД): ")
    
    found_any = False
    for task_id in planner:
        task = planner[task_id]
        if task["date"] == date_str:
            print("ID:", task_id, "| [", task["time"], "]", task["title"], "(", task["description"], ")")
            found_any = True
            
    if found_any == False:
        print("На цю дату подій не знайдено.")

def main():
    planner = load_data()

    while True:
        print("\n===== ГОЛОВНЕ МЕНЮ ПЛАНУВАЛЬНИКА =====")
        print("1. Головне меню")
        print("2. Додавання події")
        print("3. Перегляд усіх подій")
        print("4. Видалення події")
        print("5. Пошук за датою")
        print("6. Зберегти та вийти")
        
        choice = input("Виберіть дію (1-6): ")

        if choice == "1":
            pass 
        elif choice == "2":
            add_task(planner)
        elif choice == "3":
            view_tasks(planner)
        elif choice == "4":
            delete_task(planner)
        elif choice == "5":
            search_by_date(planner)
        elif choice == "6":
            save_data(planner)
            print("Дякуємо за використання планувальника! До побачення.")
            break
        else:
            print("Некоректний вибір! Будь ласка, введіть число від 1 до 6.")

if __name__ == "__main__":
    main()
