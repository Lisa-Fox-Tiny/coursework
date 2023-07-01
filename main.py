from pprint import pprint
import datetime
import requests
import json
import time
from tqdm import tqdm
class YaUploader:
    def __init__(self, token: str, token_vk):
        self.token = token
        self.token_vk = token_vk

    def upload(self, id: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        url_folder = '/'.join(url.split('/')[:-1])
        url_vk = 'https://api.vk.com/method/photos.get'
        params_vk = {
            'owner_id': id,
            'access_token': token_vk,  # токен и версия api являются обязательными параметрами во всех запросах к vk
            'album_id': 'profile',
            'count': 50,
            'extended': 1,
            'v': '5.131'
        }



        dict_photos_profile = requests.get(url_vk, params=params_vk).json()
        # pprint(dict_photos_profile)
        list_photo = dict_photos_profile['response']['items']
        size_dict = {'s': 0, 'm': 1, 'x': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'y': 7, 'z': 8, 'w': 9}
        like_list_check = []
        list_info = []
        for element in list_photo:
            if element['likes']['count'] != 0:
                if element['likes']['count'] in like_list_check:
                    filename = datetime.datetime.fromtimestamp(element['date']).strftime("%Y%m%d")
                else:
                    filename = element['likes']['count']
            else:
                filename = datetime.datetime.fromtimestamp(element['date']).strftime("%Y%m%d")
            like_list_check.append(element['likes']['count'])
            for size in element['sizes']:
                max_v = max(size['type'], key=size_dict.get)
            dict_file = {'file_name': str(filename) + '.jpg', 'size':max_v}
            list_info.append(dict_file)
            with open('info.json', 'w+') as f:
                json.dump(list_info, f, indent=2)
            path_to_file = size['url']

            for i in tqdm(list_info):
                pass

            fload_name = 'Фото'
            params_folder = {'path': fload_name}
            params = {'path': f'{fload_name}/{filename}',
                      'url': path_to_file}
            headers = {
                'Authorization': token,
                'Content-Type': 'image/jpeg'
            }
            response = requests.put(url_folder, headers=headers, params=params_folder)
            response_1 = requests.post(url, headers=headers, params=params)














if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = input('Введите токен Я.Диска:')
    with open('token.txt') as file:
        token_vk = file.read()
    uploader = YaUploader(token, token_vk)
    result = uploader.upload(int(input('Введите id пользователя vk:')))
    # print(f'Файл {path_to_file} загружен')
