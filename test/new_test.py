import requests


def test_edit():
    #тест на изменение названия задачи
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"title": "True"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()["title"] == "True"
