while True:
    user_input = input("Будь ласка, введіть число: ")
    try:
        number = float(user_input)
        print(f"Дякую! Ви ввели число: {number}")
        break
    except ValueError:
        print("Це не число. Спробуйте ще раз.")
        
        
        
        while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        break
    except ValueError:
        print("Помилка: введіть коректні числа!")

print("\nМеню:")
print("1 — +")
print("2 — -")
print("3 — *")
print("4 — /")

while True:
    choice = input("Оберіть дію (1-4): ")
    
    if choice == '1':
        print(f"Результат: {num1 + num2}")
        break
    elif choice == '2':
        print(f"Результат: {num1 - num2}")
        break
    elif choice == '3':
        print(f"Результат: {num1 * num2}")
        break
    elif choice == '4':
        if num2 == 0:
            print("Помилка: ділення на нуль неможливе!")
        else:
            print(f"Результат: {num1 / num2}")
        break
    else:
        print("Помилка: невірний вибір меню. Спробуйте ще раз.")







name = input("Введіть ваше ім'я: ")

while True:
    try:
        age = int(input("Введіть ваш вік: "))
        if 1 <= age <= 120:
            print(f"Привіт, {name}! Ваш вік: {age}")
            break
        else:
            print("Помилка: вік має бути від 1 до 120.")
    except ValueError:
        print("Помилка: введіть коректне число.")





numbers = [10, 20, 30, 40, 50]

while True:
    try:
        index = int(input("Введіть індекс (від 0 до 4): "))
        print(f"Елемент за індексом {index}: {numbers[index]}")
        break
    except ValueError:
        print("Помилка: введіть коректне ціле число.")
    except IndexError:
        print("Помилка: такого індексу не існує. Спробуйте від 0 до 4.")






filename = input("Введіть назву файлу: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Помилка: файл не знайдено.")








rate = 41.5

try:
    uah = float(input("Введіть суму в грн: "))
    usd = uah / rate
    print(f"Сума в USD: {usd}")
except ValueError:
    print("Помилка: введіть правильне число.")






try:
    number = int(input("Введіть число від 1 до 3: "))
except ValueError:
    print("Помилка: потрібно ввести ціле число.")
    number = 0

try:
    result = 100 / number
    print(f"Результат ділення 100 на ваше число: {result}")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе.")

items = ["яблуко", "банан", "апельсин"]
try:
    print(f"Ваш фрукт: {items[number - 1]}")
except IndexError:
    print("Помилка: такого елемента в списку немає.")
