import requests

account_data = {
    'owner': 'jane490@doe',
    'account_type': 2,
    'initial_balance': -50.5
}

response = requests.post('http://localhost:5000/accounts', json=account_data)

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code} - {response.text}')