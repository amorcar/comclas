import requests
import time
import asyncio

from typing import Optional, Tuple
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
api_URL_aws = "http://52.207.248.221:5000/api/task"

api_HEADERS = {
    'Content-type': 'application/json',
    'accept': 'application/json'
}

def post_task(text:str, url:str) -> Optional[str]:
    data = {'text': text}
    r = requests.post(url, headers=api_HEADERS, json=data)
    return r.json().get('info', {}).get('id', None)

def get_task_status(id:str, url:str) -> Tuple[Optional[str], Optional[str]]:
    r = requests.get(url+f'/{id}', headers=api_HEADERS)
    status = r.json().get('task_status', {}).get('status', None)
    result = r.json().get('result', {}).get('value', None)
    return (status, result)

def sync_predict(
    name: str,
    description: str,
    url:str,
):
    id = post_task(description, url)
    if id is None:
        print('Request failed')
        return
    print(f'Predicting category for {name}...')
    status, result = None, None
    while status != 'SUCCESS':
        status, result = get_task_status(id, url)
        if status == 'FAILED':
            print('Prediction failed')
            return
        time.sleep(0.5)
    print(f'{name} category: {result}')

async def async_predict(
    name:str,
    description: str,
    url: str
):
    id = post_task(description, url)
    if id is None:
        print('Request failed')
        return
    print(f'Predicting category for {name}...')
    status, result = None, None
    while status != 'SUCCESS':
        status, result = get_task_status(id, url)
        if status == 'FAILED':
            print('Prediction failed')
            return
        await asyncio.sleep(0.5)
    print(f'{name} category: {result}')


def sync_requests(url:str):
    start_time = time.time()
    sync_predict('Booking', booking, url)
    sync_predict('Amazon Prime', amazon_prime, url)
    sync_predict('Amazon Prime Video', amazon_prime_video, url)
    sync_predict('CNN', cnn, url)
    sync_predict('FBI', fbi, url)
    sync_predict("L'equipe", lequipe, url)
    sync_predict('Pornhub', pornhub, url)
    print(f'All sync predictions made in: {time.time()-start_time:.2f} seconds')

async def async_requests(url:str):
    start_time = time.time()
    await asyncio.gather(*[
        async_predict('Booking', booking, url),
        async_predict('Amazon Prime', amazon_prime, url),
        async_predict('Amazon Prime Video', amazon_prime_video, url),
        async_predict('CNN', cnn, url),
        async_predict('FBI', fbi, url),
        async_predict("L'equipe", lequipe, url),
        async_predict('Pornhub', pornhub, url),
    ])
    print(f'All async predictions made in: {time.time()-start_time:.2f} seconds')


async def main():
    # url = api_URL_container
    # url = api_URL_local
    url = api_URL_aws

    sync_requests(url)
    await async_requests(url)


if __name__ == '__main__':
    asyncio.run(main())

