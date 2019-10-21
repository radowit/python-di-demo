from dataclasses import asdict, astuple

import requests


class RandomPort:
    def __init__(self, random, max_number):
        self._random = random
        self._max_number = max_number

    def generate(self):
        return self._random.randint(1, self._max_number)


class FilePort:
    def __init__(self, filename):
        self._filename = filename

    def save(self, ticket):
        with open(self._filename, "a") as file_desc:
            file_desc.write("{0},{1}\n".format(*astuple(ticket)))


class APIPort:
    def __init__(self, host):
        self._host = host
        self.last_response = None

    def send(self, ticket):
        self.last_response = requests.post(self._host, data=asdict(ticket))
