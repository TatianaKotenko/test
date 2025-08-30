import requests

url = "https://web-agr.chitai-gorod.ru/web/api/v2/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTY2Njc4OTksImlhdCI6MTc1NjQ5OTg5OSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjM0OWFkNzhkOTg0YmExNDYwMzQ0MTYzN2Q2OWRiNDI1YmM5NzY4MWJjM2M2OTMwZjdhNjQwOTNkNjM3MGM0N2YiLCJ0eXBlIjoxMH0.owi7lG88Vrda6hp4GgfGlQQRhQZVaaOF0qiZaHnugU0"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
    }

payload = {
    "phrase": "Макс Фрай"
}

def test_change_pozitive():
    response = requests.request(
        "GET", url + 'search/search-phrase-suggests', headers=headers, json=payload
    )
    assert response.status_code == 200