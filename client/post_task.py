import requests

def post_task():
    url = "http://127.0.0.1:8000/api/task"
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    data = {'text': 'Hola jaja'}
    r = requests.post(url, headers=headers, json=data)
    print(r.status_code)
    print(r.json())


if __name__ == '__main__':
    post_task()
