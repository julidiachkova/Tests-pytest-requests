import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f3be2348a4762dd0b82073e3c0b2be7'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '8145'

def test_status_code():
    responce = requests.get(url=f'{URL}/trainers')
    assert responce.status_code == 200

def test_my_trainer_id():
    responce_get = requests.get(url=f'{URL}/trainers', params= { 'trainer_id' : TRAINER_ID })
    assert responce_get.json()['data'][0]['id'] == TRAINER_ID
