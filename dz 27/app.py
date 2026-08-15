import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.__balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Успішно зараховано: {amount}")
        else:
            print("Сума поповнення повинна бути більшою за 0")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Успішно знято: {amount}")
        elif amount > self.__balance:
            print("Недостатньо коштів на балансі")
        else:
            print("Сума зняття повинна бути більшою за 0")

    @property
    def balance(self) -> float:
        return self.__balance


class UserProfile:
    def __init__(self, email: str):
        self.__email = None
        self.email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str) -> None:
        if "@" in new_email:
            self.__email = new_email
        else:
            print("Помилка: Некоректний формат email (відсутній символ '@')")


class Battery:
    def __init__(self, initial_charge: int = 100):
        self.__charge = 100
        self.charge = initial_charge

    @property
    def charge(self) -> int:
        return self.__charge

    @charge.setter
    def charge(self, value: int) -> None:
        if 0 <= value <= 100:
            self.__charge = value
        else:
            print("Помилка: Заряд батареї повинен бути в діапазоні від 0 до 100")


class Speaker:
    def __init__(self, initial_volume: int = 5):
        self.__volume = 5
        self.volume = initial_volume

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, value: int) -> None:
        if 0 <= value <= 10:
            self.__volume = value
        else:
            print("Помилка: Гучність повинна бути в діапазоні від 0 до 10")


class Character:
    def __init__(self, initial_health: int = 100):
        self.__health = initial_health

    @property
    def health(self) -> int:
        return self.__health

    def damage(self, amount: int) -> None:
        if amount > 0:
            self.__health -= amount
            if self.__health < 0:
                self.__health = 0
            print(f"Персонаж отримав {amount} шкоди. Здоров'я: {self.__health}")

    def heal(self, amount: int) -> None:
        if amount > 0:
            self.__health += amount
            if self.__health > 100:
                self.__health = 100
            print(f"Персонаж відновив {amount} здоров'я. Здоров'я: {self.__health}")


class PasswordManager:
    def __init__(self, initial_password: str):
        if len(initial_password) >= 8:
            self.__password = initial_password
        else:
            print("Попередження: Початковий пароль занадто короткий! Встановлено тимчасовий пароль.")
            self.__password = "default_password_123"

    def change_password(self, old: str, new: str) -> None:
        if old != self.__password:
            print("Помилка: Старий пароль введено неправильно!")
        elif len(new) < 8:
            print("Помилка: Новий пароль повинен містити не менше 8 символів!")
        else:
            self.__password = new
            print("Пароль успішно змінено!")


app = FastAPI()

account = BankAccount(100.0)
user = UserProfile("admin@email.com")
battery = Battery(100)
speaker = Speaker(5)
hero = Character(100)
pm = PasswordManager("super_secret_123")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/status")
def get_status():
    return {
        "balance": account.balance,
        "email": user.email,
        "charge": battery.charge,
        "volume": speaker.volume,
        "health": hero.health
    }

class ActionModel(BaseModel):
    value: str = ""
    old: str = ""
    new: str = ""

@app.post("/api/action/{target}")
def handle_action(target: str, data: ActionModel):
    global account, user, battery, speaker, hero, pm
    
    if target == "deposit":
        account.deposit(float(data.value))
    elif target == "withdraw":
        account.withdraw(float(data.value))
    elif target == "set_email":
        user.email = data.value
    elif target == "set_charge":
        battery.charge = int(data.value)
    elif target == "set_volume":
        speaker.volume = int(data.value)
    elif target == "damage":
        hero.damage(int(data.value))
    elif target == "heal":
        hero.heal(int(data.value))
    elif target == "change_password":
        pm.change_password(data.old, data.new)
        
    return get_status()

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)


