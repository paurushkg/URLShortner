## URLShortner
This is a URLShortener Site made with help of Django

## Steps to setup this project locally

-  Make sure Python 3.x is already installed. [See here for help](https://www.python.org/downloads/).
-  Clone the repo and configure the virtual environment:
-  To know about virtualenv use this link [VirtualEnv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```
$ git clone https://github.com/paurushofficial/URLShortner.git
$ cd URLShortner
$ source .venv/bin/activate # activate virtual environment (.venv is the name, use any name as you like)
$ pip install -r requirements.txt
```

-  Set up the initial migration for our custom user models in users and build the database.

```
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
```

- To view API endpoints, go to [Swagger](http://127.0.0.1:8000/api_documentation/)
