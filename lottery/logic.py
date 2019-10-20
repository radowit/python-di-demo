class LotteryLogic:
    def __init__(self, api_port, file_port, random_port):
        self._api_port = api_port
        self._file_port = file_port
        self._random_port = random_port

    def generate_ticket(self):
        return self._random_port.generate()

    def save_ticket(self, ticket):
        self._file_port.save(ticket)
        self._api_port.send(ticket)
