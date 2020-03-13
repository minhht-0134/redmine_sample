import requests
from bs4 import BeautifulSoup
from environs import Env

env = Env()
env.read_env()

LOGIN_URL = "https://dev.sun-asterisk.com/login"

link_url = "https://dev.sun-asterisk.com/versions/4045"


def login():
    session = requests.session()
    response = session.get(LOGIN_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    authenticity_token = soup.find('input', {'name': 'authenticity_token'})['value']

    payload = {
        "username": env('REDMINE_USERNAME'),
        "password": env("REDMINE_PASSWORD"),
        "authenticity_token": authenticity_token
    }

    response = session.post(LOGIN_URL, data=payload, headers=dict(referer='/'))
    if response.url == 'https://dev.sun-asterisk.com/login':
        raise Exception("Login failure! please check username or password ")
    return session

# Login via session



if __name__ == '__main__':
    session = login()
