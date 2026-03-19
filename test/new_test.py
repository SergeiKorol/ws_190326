import requests

def test_add():
    """
    попытаться создать задачу со статусом выполнено
    сразу и убедить что так не получится.
    """
    body = {"title": "generated", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()

    assert response.status_code == 202, (
            f"Ожидался статус 202, получен {response.status_code}"
        )
    assert response_body['completed'] is not True
