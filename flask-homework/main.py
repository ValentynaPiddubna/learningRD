from flask import Flask, jsonify, abort, request, redirect, render_template, make_response
import logging
import random
from faker import Faker


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/hello')
def hello_world():
    logging.info('Handling request to /hello endpoint')
    return "Hello, world!"


@app.route('/users')
def get_users():
    fake = Faker()
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count < 1:
                raise ValueError
        except ValueError:
            return make_response(jsonify({"error": "Invalid count parameter"}), 400)
        names = [fake.name() for i in range(count)]
    else:
        names = [fake.name() for i in range(random.randint(1, 10))]
    return jsonify(names)


books = ["The Great Gatsby", "To Kill a Mockingbird", "One Hundred Years of Solitude", "Pride and Prejudice",
         "The Catcher in the Rye", "Crime and Punishment", "Beloved", "Frankenstein", "Wuthering Heights",
         "The Lord of the Rings", "The Hobbit", "Harry Potter and the Philosopher's Stone"]


@app.route('/books')
def get_books():
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count < 1:
                raise ValueError
            if count > len(books):
                raise ValueError("Sample larger than population")
        except ValueError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        selected_books = random.sample(books, count)
    else:
        num_books = random.randint(1, len(books))
        selected_books = random.sample(books, num_books)
    book_list = "<ul>"
    for book in selected_books:
        book_list += f"<li>{book}</li>"
    book_list += "</ul>"
    return book_list


@app.route('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 == 0:
        return f'The user id is {user_id}'
    else:
        abort(404)


@app.route('/books/<string:title>')
def get_book_by_title(title):
    transformed_title = title.capitalize()
    return transformed_title


@app.route('/params')
def params():

    params = request.args
    params_list = [(key, value) for key, value in params.items()]
    rows = [f"{key.ljust(12)}| {value}" for key, value in params_list]
    table = '\n'.join([f"{'parameter'.ljust(12)}| value"] + rows)
    return f"<pre>{table}</pre>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            abort(400, 'Username and password are required.')

        if len(username) < 5:
            abort(400, 'Username must be at least 5 characters long.')

        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
            abort(400, 'Password must be at least 8 characters long and contain at least 1 digit and 1 uppercase letter.')

        return redirect('/users')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
