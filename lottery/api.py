import random

from flask import Flask

from .logic import LotteryLogic
from .ports import APIPort, FilePort, RandomPort

APP = Flask(__name__)
HOSTNAME = "https://httpbin.org/post"
LOG_FILENAME = "ticket.log"
MAX_TICKET_NUMBER = 1000


@APP.route("/")
def lottery():
    logic = LotteryLogic(
        api_port=APIPort(host=HOSTNAME),
        file_port=FilePort(LOG_FILENAME),
        random_port=RandomPort(random, MAX_TICKET_NUMBER),
    )
    ticket = logic.generate_ticket()
    logic.save_ticket(ticket)
    return {"ticket_no": ticket}
