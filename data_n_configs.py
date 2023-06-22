base_url = 'petstore.swagger.io/v2'
api_key = 'test_api_22_06_2023'
status = {'available': 'available',
          'pending': 'pending',
          'sold': 'sold'}
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}
del_headers = {'accept': 'application/json',
               'api_key': api_key}
'data'
post_params = {
  "id": 345678876543,
  "category": {
    "id": 0,
    "name": "new_l"
  },
  "name": "Lucky Bastard",
  "photoUrls": [
    "no photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "new_l_1"
    }
  ],
  "status": "available"
}

put_params = {
  "id": 345678876543,
  "category": {
    "id": 0,
    "name": "new_l"
  },
  "name": "Lucky Bastard",
  "photoUrls": [
    "no photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "new_l_1"
    }
  ],
  "status": "sold"
}
