import os.path
from pprint import pprint
import requests


def get_hero():
    name = ["Hulk", "Captain America", "Thanos"]
    all_heroes = []
    for hero in name:
        url = "https://superheroapi.com/api/2619421814940190/search/" + hero
        response = requests.get(url=url)
        hero_intelligence = response.json()["results"][0]["powerstats"]["intelligence"]
        super_man = {"name": hero, "intelligence": int(hero_intelligence)}
        all_heroes.append(super_man)
    intelligence_heroes_list = sorted(all_heroes, key=lambda d: d['intelligence'], reverse=True)
    print(intelligence_heroes_list)
    print(f'Самый умный супергерой - {intelligence_heroes_list[0]["name"]}')


TOKEN = "AQAAAABZAkkMAADLW6buksKnYkbFhwEL9ab-z9M"


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path):
        file_path = os.path.normpath(file_path)
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        files = {"file": open(file_path, "rb")}
        params = {"path": file_path}
        response_url = requests.get(url=url, params=params, headers=headers)
        upload_url = response_url.json().get("href")
        response_upload = requests.put(url=upload_url, headers=headers, files=files)
        print(response_upload.status_code)


if __name__ == "__main__":
    get_hero()
    uploader = YaUploader(token=TOKEN)
    file_path = "file.docx"
    result = uploader.upload(file_path)

