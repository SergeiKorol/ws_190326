import requests


def get_v1_test():
    global id
    body = {"title": "создать задачу", "completed": False}
    response = requests.post("https://sky-todo-list.herokuapp.com/", json=body)
    response_body = response.json()
    response = requests.patch(f'https://sky-todo-list.herokuapp.com//{id}', json=body)
    assert response.status_code == 200
    assert response_body['completed'] == False

    id = response.json()['id']

    body = {"completed": True}
    response = requests.patch(f'https://sky-todo-list.herokuapp.com//{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'https://sky-todo-list.herokuapp.com//{id}', json=body)
    assert response.status_code == 200
    assert response_body['completed'] == False
