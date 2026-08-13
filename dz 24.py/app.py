from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []
book_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    global book_id_counter
    title = request.form.get('title', '').strip()
    author = request.form.get('author', '').strip()
    year = request.form.get('year', '').strip()
    genre = request.form.get('genre', '').strip()
    description = request.form.get('description', '').strip()

    if not title or not author:
        return redirect(url_for('index'))

    new_book = {
        'id': book_id_counter,
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'description': description
    }
    books.append(new_book)
    book_id_counter += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return redirect(url_for('index'))

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/about-library')
def about_library():
    return render_template('about_library.html')

if __name__ == '__main__':
    app.run(debug=True)
