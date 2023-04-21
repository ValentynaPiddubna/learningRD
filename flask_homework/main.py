import os
from flask_homework import app, db
from flask import jsonify, abort, request, redirect, render_template, make_response, session, url_for
import logging
import random
from faker import Faker
from flask_homework.models import User, Book, Purchase
from random import randint
from sqlalchemy.orm import joinedload


app.secret_key = os.getenv('SECRET_KEY')
logging.basicConfig(level=logging.INFO)


def get_username():
    """Get username from session"""
    return session.get('username')


@app.route('/hello')
def hello_world():
    logging.info('Handling request to /hello endpoint')
    username = get_username()
    if username:
        return f"Hello, {username}!"
    else:
        return redirect('/login')


@app.route('/users')
def get_users():
    fake = Faker()
    username = get_username()
    if not username:
        return redirect('/login')
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
    return render_template('users.html', names=names, username=username)


books = ["The Great Gatsby", "To Kill a Mockingbird", "One Hundred Years of Solitude", "Pride and Prejudice",
         "The Catcher in the Rye", "Crime and Punishment", "Beloved", "Frankenstein", "Wuthering Heights",
         "The Lord of the Rings", "The Hobbit", "Harry Potter and the Philosopher's Stone"]


@app.route('/books')
def get_books():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/users/<int:user_id>')
def user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users_id.html', user=user)

@app.route('/books/<int:book_id>')
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_id.html', book=book)


@app.route('/books/<string:title>')
def get_book_by_title(title):
    username = get_username()
    if not username:
        return redirect('/login')
    transformed_title = title.capitalize()
    return render_template('book_title.html', title=transformed_title, username=username)


@app.route('/params')
def params():
    username = get_username()
    if not username:
        return redirect('/login')
    params = request.args
    params_list = [(key, value) for key, value in params.items()]
    rows = [f"{key.ljust(12)}| {value}" for key, value in params_list]
    table = '\n'.join([f"{'Parameter'.ljust(12)}| Value"] + rows)
    return render_template('params.html', username=username, params=params_list, table=table)


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
        # Save the username in the session
        session['username'] = username
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

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/users_json')
def new_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


@app.route('/users_html')
def users():
    users = User.query.all()
    return render_template('users_1.html', users=users)


@app.route('/purchases')
def get_purchases():
    purchases = Purchase.query.options(joinedload(Purchase.user), joinedload(Purchase.book)).all()
    return render_template('purchases.html', purchases=purchases)


@app.route('/purchases/<int:purchase_id>')
def purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    return render_template('purchase.html', purchase=purchase)






if __name__ == '__main__':
    app.run(debug=True)

