import requests
from time import sleep
from pprint import pprint as pp

def post_task():
    url = "http://127.0.0.1:8000/api/task"
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    data = {'text': 'Hola jaja'}
    r = requests.post(url, headers=headers, json=data)
    print(r.status_code)
    pp(r.json())
    return r.json().get('id', None)

def get_task_status(id:int):
    url = f"http://127.0.0.1:8000/api/task/{id}"
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    pp(r.json())
    return r.json().get('task_status',None).get('status', None)

if __name__ == '__main__':
    print('POSTing task')
    id = post_task()
    if id is None:
        id = 0
    sleep(1)
    print(f'Getting task [{id}]')
    status = get_task_status(id)
    pp(f'Status: {status}')
    sleep(10)
    print(f'Getting task [{id}]')
    status = get_task_status(id)
    pp(f'Status: {status}')
