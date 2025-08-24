import requests
#СОЗДАНИЕ НОВОГО ПРОЕКТА

url = "https://ru.yougile.com"
token = "ry5j1+HvUJiq6NpBA-ILi8vfJ5YBEZr9AzWaFrzAmq7jYQk7U4V8zCGU6dez9vne"
payload = {
    "title": "My new progect",
    "users": {
        "625da618-ccd2-43f2-9900-3c39368a0aaa": "worker"
        }
    }
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}


def test_progect_pozitive():
    response = requests.request(
        "POST", url + '/api-v2/projects', json=payload, headers=headers
    )
    assert response.status_code == 201


def test_progect_negative():
    response = requests.request(
        "DELETE", url + '/api-v2/projects', json=None, headers=headers
    )
    assert response.status_code == 404
