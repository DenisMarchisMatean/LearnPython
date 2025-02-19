import pytest
from flask import Flask
from FlaskWeatherAPI.app import app  # Adjust the import based on your project structure


def test_show_days_per_month_per_year(mocker):
    client = app.test_client()
    mock_response = {
        "days": [
            {
                "datetime": "2025-02-01",
                "hours": [
                    {"datetime": "00:00", "snow": 0},
                    {"datetime": "01:00", "snow": 5.2},
                    {"datetime": "02:00", "snow": 0}
                ]
            }
        ]
    }

    mocker.patch("FlaskWeatherAPI.app.requests.get",
                 return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    response = client.get("/show_days_per_month_per_year?city=Clus-Napoca&country_shorten=RO&month=02&year=2025")

    assert response.status_code == 200
    json_data = response.get_json()
    assert "2025-02-01" in json_data
    assert "01:00" in json_data["2025-02-01"]
    assert json_data["2025-02-01"]["01:00"] == 5.2
