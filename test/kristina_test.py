import requests

url = "https://todo-app-sky.herokuapp.com/"


def test_get_list_with_deleted_task():
    # Тест на проверку статус-кода 404 при получении списка задач после создания и удаления созданной задачи.
    body = {"title": "Создать задачу", "completed": False}
    response = requests.post(url, json=body)
    response_body = response.json()
    assert response.status_code == 202

    task_id = response_body["id"]
    delete_response = requests.delete(f'{url}{task_id}')
    assert delete_response.status_code == 204

    get_response = requests.get(f'{url}{task_id}')
    assert get_response.status_code == 404
