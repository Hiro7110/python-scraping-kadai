# requestsモジュールをインストール
!pip install requests
import requests

# geopyモジュールをインストール
!pip install geopy
import geopy
from geopy.geocoders import Nominatim

# jsonモジュールをimport
import json

# getpassモジュールをインストール
from getpass import getpass

# api_keyを入力するための表示
api_key = getpass("Input API key: ")

# 住所を指定するための表示
search_word = input("Input search word: ")

# search_wordの住所を取得する
geolocator = Nominatim(user_agent="test")
location = geolocator.geocode(search_word)

# print(location.address)
# print(location.latitude)
# print(location.longitude)

# define latitude and longitude
latitude = location.latitude
longitude = location.longitude

# Nearby Searchで使用するurlを定義
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# resuestを使用して指定の駅名の周辺のレストラン情報を取得
response = requests.get(
    url,
    params={
        "key" : api_key,
        "location" : f'{latitude},{longitude}',
        "keyword" : "restaurant",
        "language" : "ja",
        "radius" : 500,
    }
)

# print(response.text)

# 取得した情報をjsonに変換
json_data = json.loads(response.text)

# 名前とレーティングと住所のみを出力
i = 1

for result in json_data["results"]:
    name = result["name"]
    rating = result["rating"]
    vicinity = result["vicinity"]
    print(f"{i}店舗目")
    print(name)
    print(rating)
    print(vicinity)
    print()
    i += 1

