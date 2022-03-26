import requests
from time import sleep

def post_task():
    url = "http://127.0.0.1:8000/api/task"
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    data = {'text': 'Hola jaja'}
    r = requests.post(url, headers=headers, json=data)
    print(r.status_code)
    print(r.json())
    return r.json()['id']

def get_task_status(id:int):
    url = f"http://127.0.0.1:8000/api/task/{id}"
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())
    return r.json()['status']

if __name__ == '__main__':
    print('POSTing task')
    id = post_task()
    sleep(1)
    print(f'Getting task [{id}]')
    get_task_status(id)
    sleep(10)
    print(f'Getting task [{id}]')
    get_task_status(id)
