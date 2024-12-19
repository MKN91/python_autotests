import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = '85c61691b31b2e0e407f971bd378a8b0'
Trainerid = '12607'
headers = {
    'Content-Type': 'application/json',
    'trainer_token': token
}

def test_code_200():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':Trainerid})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id':Trainerid})
    assert response_get.json()["data"][0]["trainer_name"] == "Turkleton"                           
