from flask import Flask

app = Flask(__name__)
app.secret_key = 'a very great secret'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////database/database.sqlite'

@app.route('/')
def index():
    return "welcome screen"

@app.route('/register')
def register():
    return "register"


@app.route('/login')
def login():
    return 'login'

@app.route('/guest')
def guest():
    return 'guest page'
if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)

