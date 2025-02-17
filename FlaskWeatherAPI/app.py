from flask import Flask
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

x = requests.get('https://w3schools.com')
print('The status code is: ', x.status_code)


@app.get('/')
def index():
    pass


@app.post('/add')
def add():
    pass
