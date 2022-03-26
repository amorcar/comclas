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

api_URL = "http://127.0.0.1:8000/api/task"
api_HEADERS = {
    'Content-type': 'application/json',
    'accept': 'application/json'
}

def post_task(text:str) -> Optional[str]:
    data = {'text': text}
    r = requests.post(api_URL, headers=api_HEADERS, json=data)
    return r.json().get('info', {}).get('id', None)

def get_task_status(id:int) -> Tuple[Optional[str]]:
    r = requests.get(api_URL+f'/{id}', headers=api_HEADERS)
    status = r.json().get('task_status', {}).get('status', None)
    result = r.json().get('result', {}).get('value', None)
    return (status, result)

def predict_company(
    name: str,
    description: str
):
    id = post_task(description)
    if id is None:
        print('Request failed')
        return
    print(f'Predicting category for {name}...')
    status = ''
    while status != 'SUCCESS':
        status, result = get_task_status(id)
        sleep(0.5)
    print(f'{name} category: {result}')

if __name__ == '__main__':
    predict_company('Booking', booking)
    predict_company('Amazon Prime', amazon_prime)
    predict_company('Amazon Prime Video', amazon_prime_video)
    predict_company('CNN', cnn)
    predict_company('FBI', fbi)
    predict_company("L'equipe", lequipe)
    predict_company('Pornhub', pornhub)

