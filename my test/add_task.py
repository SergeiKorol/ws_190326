import requests

def test_add():
    body = {"title": "Создать задачу", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    assert response.status_code == 202
    assert response_body['completed'] == False

    id = response.json()["id"]

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response_body['completed'] == True
