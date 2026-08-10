import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/planner')
def planner():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY is_completed ASC, id DESC').fetchall()
    conn.close()
    return render_template('planner.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if title:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)',
            (title, description, created_at)
        )
        conn.commit()
        conn.close()
    
    return redirect(url_for('planner'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET is_completed = 1 - is_completed WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('planner'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('planner'))

if __name__ == '__main__':
    app.run(debug=True)
