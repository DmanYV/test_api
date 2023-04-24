import requests
from pytest_voluptuous import S

from schemas.api import booking

def test_booking():
    responce = requests.get('https://restful-booker.herokuapp.com/booking/1')
    assert S(booking) == responce.json()
