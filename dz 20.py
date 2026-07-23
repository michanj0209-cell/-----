class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сума поповнення має бути більшою за 0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів або некоректна сума")

    @property
    def balance(self):
        return self.__balance


class UserProfile:
    def __init__(self, email):
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            print("Помилка: Некоректний формат Email (відсутній символ '@')")


class Battery:
    def __init__(self, charge=100):
        self.__charge = None
        self.charge = charge

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, value):
        if 0 <= value <= 100:
            self.__charge = value
        else:
            print("Помилка: Значення заряду має бути в межах від 0 до 100")


class Speaker:
    def __init__(self, volume=5):
        self.__volume = None
        self.volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if 0 <= value <= 10:
            self.__volume = value
        else:
            print("Помилка: Гучність має бути в діапазоні від 0 до 10")


class Character:
    def __init__(self, initial_health=100):
        self.__health = initial_health

    def damage(self, amount):
        if amount > 0:
            self.__health -= amount
            if self.__health < 0:
                self.__health = 0
        else:
            print("Кількість шкоди має бути більшою за нуль")

    def heal(self, amount):
        if amount > 0:
            self.__health += amount
        else:
            print("Кількість зцілення має бути більшою за нуль")

    @property
    def health(self):
        return self.__health


class PasswordManager:
    def __init__(self, initial_password):
        self.__password = initial_password

    def change_password(self, old, new):
        if old != self.__password:
            print("Помилка: Старий пароль вказано неправильно!")
            return False
            
        if len(new) < 8:
            print("Помилка: Новий пароль має містити не менше 8 символів!")
            return False
            
        self.__password = new
        print("Пароль успішно змінено.")
        return True


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(f"Баланс рахунку: {account.balance}")
    
    user = UserProfile("user@example.com")
    user.email = "valid_address@mail.com"  
    
    laptop_battery = Battery(85)
    laptop_battery.charge = 95          
    
    sound = Speaker(7)
    sound.volume = 9                    
    
    hero = Character(100)
    hero.damage(40)
    hero.heal(15)
    print(f"Здоров'я персонажа: {hero.health}")
    
    pm = PasswordManager("my_secret_key")
    pm.change_password("my_secret_key", "strong_228") 


