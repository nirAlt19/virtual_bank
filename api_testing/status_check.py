import requests

response = requests.post('http://localhost:5000/status', json={})

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code} - {response.text}')