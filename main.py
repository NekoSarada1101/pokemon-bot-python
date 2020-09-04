import json
import requests
import random
from setting_secret import *


def do_post(e):
    token = e.form.get('token')
    if token != SLACK_TOKEN and token != IFTTT_TOKEN:
        raise Exception("not allowed token:" + str(token))

    id = str(random.randint(1, 807))

    poke_json = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon/" + id).text)
    species_json = json.loads(requests.get(poke_json['species']['url']).text)

    for index in range(len(species_json['names'])):
        if species_json['names'][index]['language']['name'] == "ja":
            ja_name = species_json['names'][index]['name']
            break

    for index in range(len(species_json['flavor_text_entries'])):
        if species_json['flavor_text_entries'][index]['language']['name'] == "ja":
            ja_flavor_text = species_json['flavor_text_entries'][index]['flavor_text']
            break

    data = {
        "attachments": [
            {
                "color": get_colorcode(poke_json['types'][0]['type']['name']),
                "blocks": [
                    {
                        "type": 'image',
                        "image_url": poke_json['sprites']['front_default'],
                        "alt_text": 'pokemon',
                    },
                    {
                        "type": 'context',
                        "elements": [
                            {
                                "type": 'mrkdwn',
                                "text": 'No.' + id + '\n*' + ja_name + '* _' + poke_json['name'] + '_',
                            },
                        ],
                    },
                    {
                        "type": 'section',
                        "text": {
                            "type": 'mrkdwn',
                            "text": ja_flavor_text,
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
                                "url": 'https://yakkun.com/swsh/zukan/n' + id,
                                "value": 'click_me_123',
                            },
                        ],
                    },
                ],
            },
        ],
    }
    json_data = json.dumps(data).encode("utf-8")
    requests.post(POKEMON_URL, json_data)
    return ""


def get_colorcode(type):
    color_code = {
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
    return color_code[type]


def main():
    do_post("e")


if __name__ == "__main__":
    main()
