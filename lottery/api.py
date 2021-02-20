import random
from dataclasses import asdict

from flask import Flask

from .logic import TicketGenerator, TicketSaver
from .ports import APIPort, FilePort, RandomPort

APP = Flask(__name__)
HOSTNAME = "https://httpbin.org/post"
LOG_FILENAME = "ticket.log"
MAX_TICKET_NUMBER = 1000


@APP.route("/")
def lottery():
    ticket_generator = TicketGenerator(
        random_port=RandomPort(random, MAX_TICKET_NUMBER)
    )
    ticket_saver = TicketSaver(
        api_port=APIPort(host=HOSTNAME), file_port=FilePort(LOG_FILENAME)
    )
    ticket = ticket_generator.generate_ticket()
    ticket_saver.save_ticket(ticket)
    return asdict(ticket)
