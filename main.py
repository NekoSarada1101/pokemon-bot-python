import json
import requests
import random
from slack_webhook_url import *


def do_post():
    pokemon_id = str(random.randint(1, 808))  # type: str
    pokemon_response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_id).json()  # type: json

    image_url = pokemon_response["sprites"]["front_default"]
    species_url = pokemon_response["species"]["url"]  # type: str
    type_name = pokemon_response["types"][0]["type"]["name"]  # type: str
    color_code = get_color_code(type_name)  # type: str

    print("image_url=" + image_url)
    print("species_url=" + species_url)
    print("type_name=" + type_name)
    print("color_code=" + color_code)

    species_response = requests.get(species_url).json()  # type: json

    ja_name = ""  # type: str
    for names in species_response["names"]:
        if names["language"]["name"] == "ja":
            ja_name = names["name"]
            break

    en_name = ""  # type: str
    for names in species_response["names"]:
        if names["language"]["name"] == "en":
            en_name = names["name"]
            break

    flavor_text = ""  # type: str
    for flavor_text_entry in species_response["flavor_text_entries"]:
        if flavor_text_entry["language"]["name"] == "ja":
            flavor_text = flavor_text_entry["flavor_text"]
            break

    print("ja_name=" + ja_name)
    print("en_name=" + en_name)
    print("flavor_text=" + flavor_text)

    data = {  # type: dict
        "attachments": [
            {
                "color": color_code,
                "blocks": [
                    {
                        "type": 'image',
                        "image_url": image_url,
                        "alt_text": 'pokemon',
                    },
                    {
                        "type": 'context',
                        "elements": [
                            {
                                "type": 'mrkdwn',
                                "text": 'No.' + pokemon_id + '\n*' + ja_name + '* _' + en_name + '_',
                            },
                        ],
                    },
                    {
                        "type": 'section',
                        "text": {
                            "type": 'mrkdwn',
                            "text": flavor_text,
                        },
                    },
                    {
                        "type": 'actions',
                        "elements": [
                            {
                                "type": 'button',
                                "text": {
                                    "type": 'plain_text',
                                    "text": '詳しく見る',
                                },
                                "url": "https://yakkun.com/swsh/zukan/n" + pokemon_id,
                                "value": 'click_me_123',
                            },
                        ],
                    },
                ],
            },
        ],
    }
    json_data = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, json_data)  # type: response
    print(response)
    return ""


def get_color_code(type_name: str) -> str:
    color_code = {  # type: dict
        'normal': '#979797',
        'fighting': '#B01E1F',
        'flying': '#7E80EC',
        'poison': '#8C278E',
        'ground': '#D7A955',
        'rock': '#A9912C',
        'bug': '#8BAD19',
        'ghost': '#5C4286',
        'steel': '#5B7C8A',
        'fire': '#E96B25',
        'water': '#5579EC',
        'grass': '#24B820',
        'electric': '#F6C826',
        'psychic': '#F33D75',
        'ice': '#89D0CF',
        'dragon': '#5B0FF6',
        'dark': '#3F3834',
        'fairy': '#EA83D0'
    }
    return color_code[type_name]


if __name__ == "__main__":
    do_post()
