from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ласкаво просимо! Це головна сторінка мого локального сервера."

@app.route('/about')
def about():
    return "Інформація про автора: [Абоба], початківець веб-розробник."

@app.route('/skills')
def skills():
    return "Мої навички: Python, Flask, HTML, CSS, SQL."

@app.route('/contact')
def contact():
    return "Контактна інформація: email@example.com, Telegram: @username"

@app.route('/temperature/<int:t>')
def check_temperature(t):
    if t < 0:
        return "Мороз"
    elif 0 <= t <= 20:
        return "Прохолодно"
    elif 20 < t < 30:
        return "Тепло"
    else:
        return "Спека"

@app.route('/math/<operation>/<int:a>/<int:b>')
def calculator(operation, a, b):
    if operation == 'add':
        result = a + b
        return str(result)
    elif operation == 'sub':
        result = a - b
        return str(result)
    elif operation == 'mul':
        result = a * b
        return str(result)
    elif operation == 'div':
        if b == 0:
            return "Помилка: Ділення на нуль!", 400
        result = a / b
        if result.is_integer():
            return str(int(result))
        return str(result)
    else:
        return "Невідома операція! Доступні: add, sub, mul, div", 400

if __name__ == '__main__':
    app.run(debug=True)
