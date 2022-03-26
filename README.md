# comclas
API to predict the category of companies by their description

To run:
```bash
$ git clone https://github.com/amorcar/comclas.git
$ cd comclas/
$ docker-compose up -d --build
```

To predict:
```bash
$ python3 -m venv venv --prompt comclas
$ source venv/bin/activate
$ pip install -r app/requirements.txt
$ python client/run_examples.py
```
