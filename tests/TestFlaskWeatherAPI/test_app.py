import pytest
from FlaskWeatherAPI import app


def test_app_no_query_params():
    response = app.app.test_client().get('/show_days_per_month_per_year')
    assert response.status_code == 400


def test_app_query_params_to_many_requests():
    response = app.app.test_client().get('/show_days_per_month_per_year?city=Cluj-Napoca&country_shorten=RO&month=1&year=2025')
    assert response.status_code == 429
