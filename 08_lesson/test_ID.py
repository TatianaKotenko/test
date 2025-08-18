import requests


url = "https://ru.yougile.com"
token = "ry5j1+HvUJiq6NpBA-ILi8vfJ5YBEZr9AzWaFrzAmq7jYQk7U4V8zCGU6dez9vne"
id = "c5d90e0f-1956-45ff-9228-810905ec156f"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}" 
    }

def test_pozitive_id_company():
    response = requests.request("GET", url + f'/api-v2/projects/{id}', headers=headers)
    assert response.status_code == 200

def test_negative_id_company():
    response = requests.request("GET", url + f'/api-v2/projects/{token}', headers=headers)
    assert response.status_code == 404