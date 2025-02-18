import os
import time
import datetime
from pprint import pprint
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

@app.get('/show_days_per_month_per_year')
def index():
    city = request.args.get('city')
    country_shorten = request.args.get('country_shorten')
    month = request.args.get('month')
    year = request.args.get('year')

    if not all([city, country_shorten, month, year]):
        return jsonify({"error": "Missing required query parameters"}), 400



    start_date =int(time.mktime(datetime.datetime.strptime(f'01/{month}/{year}',"%d/%m/%Y").timetuple()))
    end_date =int(time.mktime(datetime.datetime.strptime(f'10/{month}/{year}',"%d/%m/%Y").timetuple()))

    print(start_date)
    print(end_date)

    url = f"{os.getenv("WEATHER_API_TIMELINE_BASE_URL")}/{city},{country_shorten}/{start_date}/{end_date}?key={os.getenv("WEATHER_API_KEY")}"

    response = requests.get(url)
    pprint(response)

    if response.status_code == 200:
        processed_data = {}
        data = response.json()
        for day in data.days:
            processed_data[day.get("datetime")] = {}
            for hours in day.get("hours"):
                if hours.get("snow") != 0:
                    processed_data[day.get("datetime")][hours.get("datetime")] = hours.get("snow")

        return jsonify(processed_data)
    else:
        return jsonify(
            {"error": "Failed to fetch weather data", "status_code": response.status_code}), response.status_code


@app.post('/add')
def add():
    pass
