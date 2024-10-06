import requests

user_data = {
    'email': 'jane124@doe',
    'hashed_password': 'password123'
}

response = requests.post('http://localhost:5000/users/login', json=user_data)

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code} - {response.text}')