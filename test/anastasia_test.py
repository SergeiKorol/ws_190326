import requests


def create_delete_task():
  
    body = {"title": "temporary task", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{task_id}')
    assert response.status_code == 204

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{task_id}')
    assert response.status_code == 404
