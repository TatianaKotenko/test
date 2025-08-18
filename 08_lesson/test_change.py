import requests


url = "https://ru.yougile.com"
token = "ry5j1+HvUJiq6NpBA-ILi8vfJ5YBEZr9AzWaFrzAmq7jYQk7U4V8zCGU6dez9vne"
id = "c5d90e0f-1956-45ff-9228-810905ec156f"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
    }

payload = {
    "deleted": False,
    "title": "My modified project",
    "users": {
        "625da618-ccd2-43f2-9900-3c39368a0aaa": "worker"
    }
}


def test_change_pozitive():
    response = requests.request(
        "PUT", url + f'/api-v2/projects/{id}', json=payload, headers=headers
    )
    assert response.status_code == 200


def test_change_negative():
    response = requests.request(
        "PUT", url + f'/api-v2/projects/{id}', json=headers, headers=headers
    )
    assert response.status_code == 400
