from random import randint

import requests
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def lottery():
    ticket_no = randint(1, 1000)
    with open('ticket.log', 'a') as ticket_log:
        ticket_log.write(f'{ticket_no}\n')
    data = {'ticket_no': ticket_no}
    requests.post('https://httpbin.org/post', data=data)
    return data
