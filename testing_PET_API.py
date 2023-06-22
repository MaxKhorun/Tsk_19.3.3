import requests
import json
from data_n_configs import base_url, id_pet, post_params, status, headers, put_params


resp = requests.get(f'https://{base_url}/pet/findByStatus?status={status}',\
                    headers= headers)
if 'application/json' in resp.headers['Content-Type']:
    resp_mod = resp.json()
else:
    resp_mod = resp.text
print('res 1 -', resp_mod)
'Не забыть в запросах проставить заголовки!!!'
'тестирование ГЕТ'
# resp_getPet = requests.get(f'https://{base_url}/pet/{id_pet}', headers=headers)
# print('res 2 -', resp_getPet.json())

'тестирование ПОСТ'
# resp_postPet = requests.post(f'https://{base_url}/pet', headers=headers, data=json.dumps(post_params))
# print('res post -', resp_postPet.json())

'тестирование delete'
# r_delete_Pet = requests.delete(f'https://{base_url}/pet/{id_pet}', headers=headers)
# print('res delete - ', r_delete_Pet)

'тестирование put'
r_put_Pet = requests.put(f'https://{base_url}/pet', headers=headers, data=json.dumps(put_params))
print('res pu -', r_put_Pet.json())