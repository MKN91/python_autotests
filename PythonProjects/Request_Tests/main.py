import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '85c61691b31b2e0e407f971bd378a8b0'
headers = {
    'Content-Type': 'application/json',
    'trainer_token': token
}
           
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "162499",
    "name": "grookey10",
    "photo_id": 4
}
body_pokeball = {
    "pokemon_id": "162499"
}
'''response = requests.post(url = f'{URL}/pokemons', headers = headers, json = body_create)
print(response.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = headers, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = headers, json = body_pokeball)
print(response_pokeball.text)