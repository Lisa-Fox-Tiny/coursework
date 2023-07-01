# from pprint import pprint
#
# import requests
#
# with open('token.txt') as file:
#     token_vk = file.read()
# url_vk = 'https://api.vk.com/method/photos.get'
# params_vk = {
#             'owner_id': '1',
#             'access_token': token_vk,  # токен и версия api являются обязательными параметрами во всех запросах к vk
#             'album_id': 'profile',
#             'count': 50,
#             'v': '5.131'
# }
# res = requests.get(url_vk, params=params_vk)
# pprint(res.json())

# a = 'Первый - второй - третий'
# print('-'.join(a.split('-')[:-1]))
