import requests

headers = {'Content-Type': 'application/json; charset=utf-8'}


def add_user(username):
    data = {
        "username": username
    }
    response = requests.post('http://localhost:8081/api/v1/users/user', json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return response.json()
