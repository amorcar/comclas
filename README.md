# comclas
API to predict the category of companies by their description

[Docs + Try it out](http://52.207.248.221:5000/docs)

To run:
```bash
$ git clone https://github.com/amorcar/comclas.git
$ cd comclas/
$ docker-compose up -d --build
```

To run the examples:
```bash
$ python3 -m venv venv --prompt comclas
$ source venv/bin/activate
$ pip install -r app/requirements.txt
$ python client/run_examples.py
```
Output:
```text
Predicting category for Booking...
Booking category: Travel
Predicting category for Amazon Prime...
Amazon Prime category: E-Commerce
Predicting category for Amazon Prime Video...
Amazon Prime Video category: Streaming Services
Predicting category for CNN...
CNN category: News
```

Build with SKLearn, FastAPI, Celery, Redis, Docker & Docker-compose.
