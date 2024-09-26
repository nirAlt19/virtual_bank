import requests
import random

password = 'password123'

user_data = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'email': 'jane' + str(random.randint(1, 1000)) + '@doe',
    'password': password
}

response = requests.post('http://localhost:5000/users', json=user_data)

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code} - {response.text}')