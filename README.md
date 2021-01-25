# random-pokemon-slack-bot
<img width=300px src="https://user-images.githubusercontent.com/46714670/105172645-44da9e00-5b63-11eb-8211-c7067311538d.png"> <img width=300px src="https://user-images.githubusercontent.com/46714670/105174038-49a05180-5b65-11eb-8281-c4dae8242259.png">

## 概要
ランダムなポケモンの情報と画像をSlackで表示する。

## 開発環境
* Python 3.8
* [PokeAPI](https://pokeapi.co/)

## 使用方法
リポジトリをクローンする。
```
git clone https://github.com/NekoSarada1101/random-pokemon-slack-bot.git
```
[slack_webhook_url.py](https://github.com/NekoSarada1101/random-pokemon-slack-bot/blob/main/slack_webhook_url.py) の`SLACK_WEBHOOK_URL`を自分のSlackのWebhook URLに書き換える。

ディレクトリを移動し、実行する。
```
cd random-pokemon-slack-bot
python main.py
```

## ライセンス
[MIT](https://github.com/NekoSarada1101/random-pokemon-slack-bot/blob/main/LICENSE)
