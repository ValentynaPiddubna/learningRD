from flask_homework import app

# TODO: test todo

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))