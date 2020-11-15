import json
import requests
import random
from setting_secret import *
from google.cloud import firestore


def do_post(e):
    token = e.form.get('token')
    if token != SLACK_TOKEN and token != IFTTT_TOKEN:
        raise Exception("not allowed token:" + str(token))

    id = str(random.randint(1, 808))

    db = firestore.Client.from_service_account_json('credentials.json')
    doc = db.collection('pokemon').document(id).get().to_dict()
    print(doc)

    data = {
        "attachments": [
            {
                "color": get_colorcode(doc['types'][0]),
                "blocks": [
                    {
                        "type": 'image',
                        "image_url": doc['image'],
                        "alt_text": 'pokemon',
                    },
                    {
                        "type": 'context',
                        "elements": [
                            {
                                "type": 'mrkdwn',
                                "text": 'No.' + str(doc['id']) + '\n*' + doc['ja_name'] + '* _' + doc['en_name'] + '_',
                            },
                        ],
                    },
                    {
                        "type": 'section',
                        "text": {
                            "type": 'mrkdwn',
                            "text": doc['flavor_text'],
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
                                "url": doc['url'],
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


if __name__ == "__main__":
    do_post()
