import requests

def test_update():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_id = response.json()['id']

    updated_body = {"title": "generated_up", "completed": True}
    requests.patch("https://todo-app-sky.herokuapp.com/", json=updated_body)
    response_update = requests.get("https://todo-app-sky.herokuapp.com/")
    response_update_id = response_update.json()['id']

    # Получить из ответа id не получается

    assert response_id == response_update_id
