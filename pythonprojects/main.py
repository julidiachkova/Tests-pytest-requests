import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f3be2348a4762dd0b82073e3c0b2be7'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": -1
}
response_create = {"message":"Покемон создан",
                   "id": "115541"
                   }
pokemon_id = response_create["id"]
body_change = {
    "pokemon_id": pokemon_id,
    "name": "Пуля",
    "photo_id": -1
}
body_add = {
    "pokemon_id": pokemon_id
}

response = requests.post (url = f'{URL}/pokemons', headers= HEADER, json = body_create)#Создание покемона (POST  /pokemons)
print (response.text)

response = requests.put (url = f'{URL}/pokemons', headers= HEADER, json = body_change)#Смена имени покемона (PUT /pokemons)
print (response.text)

response = requests.post (url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add)#Поймать покемона в покебол (POST /trainers/add_pokeball)
print (response.text)