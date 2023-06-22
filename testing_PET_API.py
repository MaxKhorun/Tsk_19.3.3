import requests
import json
from data_n_configs import base_url, post_params,\
    status, headers, put_params, del_headers
def check_the_resp(r):
    if 'application/json' in r.headers['Content-Type']:
        resp_mod = r.json()
    else:
        resp_mod = r.text
    return resp_mod

'''Тестирование ГЕТ-запроса по статусу питомца'''
resp_get_by_Status = requests.get(f"https://{base_url}/pet/findByStatus?status={status['available']}",
                    headers=headers)
resp_1 = check_the_resp(resp_get_by_Status)
pet_ID = resp_1[0]['id']
print('res 1: тестирование ГЕТ-запроса по статусу питомца - ', resp_1)

'''тестирование ГЕТ-запроса. Find pet by ID'''
resp_getPet = requests.get(f'https://{base_url}/pet/{pet_ID}', headers=headers)
resp_2 = check_the_resp(resp_getPet)

print('res 2: find pet by status -', resp_2)

'''тестирование ПОСТ.' \
Add a new pet to the store'''
resp_postPet = requests.post(f'https://{base_url}/pet', headers=headers, data=json.dumps(post_params))
resp_3 = check_the_resp(resp_postPet)
posted_ID = resp_3['id']
posted_name = resp_3['name']

print('res 3: post a new pet to the store - ', resp_3,
      '\nposted ID: ', posted_ID,
      '\nposted name: ', posted_name)

'''тестирование put.
Update an existing pet'''
r_put_Pet = requests.put(f'https://{base_url}/pet', headers=headers, data=json.dumps(put_params))
resp_4 = check_the_resp(r_put_Pet)

print('res 4: Update an existing pet -', resp_4,
      '\nstatus: ', resp_4['status'])

'''тестирование delete'''
r_delete_Pet = requests.delete(f'https://{base_url}/pet/{pet_ID}', headers=del_headers)
resp_5 = check_the_resp(r_delete_Pet)

print('res delete - ', resp_5)
