from .entities import Ticket


class TicketGenerator:
    def __init__(self, random_port):
        self._random_port = random_port

    def generate_ticket(self):
        return Ticket(ticket_id=self._random_port.generate())


class TicketSaver:
    def __init__(self, api_port, file_port):
        self._api_port = api_port
        self._file_port = file_port

    def save_ticket(self, ticket):
        self._file_port.save(ticket)
        self._api_port.send(ticket)
