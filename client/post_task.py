import requests
from typing import Optional, Tuple
from time import sleep
from pprint import pprint as pp

from company_descriptions import (
    booking,
    amazon_prime,
    amazon_prime_video,
    cnn,
    lequipe,
    fbi,
    pornhub,
)

api_URL_container = "http://127.0.0.1:8004/api/task"
api_URL_local = "http://127.0.0.1:8000/api/task"

api_HEADERS = {
    'Content-type': 'application/json',
    'accept': 'application/json'
}

def post_task(text:str, url:str) -> Optional[str]:
    data = {'text': text}
    r = requests.post(url, headers=api_HEADERS, json=data)
    return r.json().get('info', {}).get('id', None)

def get_task_status(id:int, url:str) -> Tuple[Optional[str]]:
    r = requests.get(url+f'/{id}', headers=api_HEADERS)
    status = r.json().get('task_status', {}).get('status', None)
    result = r.json().get('result', {}).get('value', None)
    return (status, result)

def predict_company(
    name: str,
    description: str,
    url:str,
):
    id = post_task(description, url)
    if id is None:
        print('Request failed')
        return
    print(f'Predicting category for {name}...')
    status = ''
    while status != 'SUCCESS':
        status, result = get_task_status(id, url)
        sleep(0.5)
    print(f'{name} category: {result}')

if __name__ == '__main__':
    url = api_URL_container
    # url = api_URL_local

    predict_company('Booking', booking, url)
    predict_company('Amazon Prime', amazon_prime, url)
    predict_company('Amazon Prime Video', amazon_prime_video, url)
    predict_company('CNN', cnn, url)
    predict_company('FBI', fbi, url)
    predict_company("L'equipe", lequipe, url)
    predict_company('Pornhub', pornhub, url)

