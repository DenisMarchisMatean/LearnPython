from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

# How can i print something in console ?
# Where do i see the request that has been made ?
# How do i make a constant file for strings ?
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)

x = requests.get('https://w3schools.com')
print('The status code is: ', x.status_code)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column('datetime', db.String)
    conditions = db.Column('conditions', db.String)
    icon = db.Column('icon', db.String)
    datetimeEpoch = db.Column('datetimeEpoch', db.Float)
    temp = db.Column('temp', db.Float)
    feelslike = db.Column('feelslike', db.Float)
    humidity = db.Column('humidity', db.Float)
    dew = db.Column('dew', db.Float)
    precip = db.Column('precip', db.Float)
    precipprob = db.Column('precipprob', db.Float)
    snow = db.Column('snow', db.Float)
    snowdepth = db.Column('snowdepth', db.Float)
    windspeed = db.Column('windspeed', db.Float)
    winddir = db.Column('winddir', db.Float)
    pressure = db.Column('pressure', db.Float)
    visibility = db.Column('visibility', db.Float)
    cloudcover = db.Column('cloudcover', db.Float)
    seen = db.Column('seen', db.Boolean)
    address = db.Column('address', db.String)
    latitude = db.Column('latitude', db.Float)
    timezone = db.Column('timezone', db.String)
    longitude = db.Column('longitude', db.Float)
    description = db.Column('description',db.String)
    resolvedAddress = db.Column('resolvedAddress', db.String)

db.drop_all()
db.create_all()
@app.get('/')
def index():
    city = "Cluj-Napoca"
    country_shorten = "RO"
    start_date = 1601510400
    end_date = 1601510401
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},{country_shorten}/{start_date}/{end_date}?key=VJWG7USK9FMZNP9BB27NUADAK")
    weather = db.session.query(Weather).all()
    return render_template("base.html", weather=weather, data=response.json())


@app.post('/add')
def add():
    print('The status code is: ', x.status_code)
    new_weather = Weather(
        seen=True,
        address="request.form['address']",
        latitude=10,
        timezone="request.form['timezone']",
        longitude=10,
        description="request.form['description']",
        resolvedAddress="request.form['resolvedAddress']",
    )
    db.session.add(new_weather)
    db.session.commit()
    return redirect(url_for('index'))

# @add.update('/mark_as_seen/<int:id>')
# def update(weather_id):
#     weather = db.session.query(Weather).filter_by(id=weather_id).first()
#     weather.seen = not weather.seen
#     db.session.commit()
#     return redirect(url_for('index'))
