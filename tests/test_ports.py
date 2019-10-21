from datetime import datetime
from random import Random
from tempfile import mkstemp

from pytest import mark

from lottery.entities import Ticket
from lottery.ports import APIPort, FilePort, RandomPort


def test_random_port():
    port = RandomPort(Random(10000), 1000)

    assert port.generate() == 592


@mark.integration
def test_file_port():
    __, path = mkstemp()
    port = FilePort(path)

    port.save(Ticket(ticket_id=123, creation_time=datetime(2020, 10, 11, 10, 22, 1)))
    port.save(Ticket(ticket_id=987, creation_time=datetime(2020, 10, 11, 11, 22, 1)))

    with open(path, "r") as desc:
        assert desc.read() == "123,2020-10-11 10:22:01\n987,2020-10-11 11:22:01\n"


@mark.integration
def test_api_port():
    port = APIPort("https://httpbin.org/post")

    port.send(Ticket(ticket_id=123, creation_time=datetime(2020, 10, 11, 10, 22, 1)))

    assert port.last_response.status_code == 200
    assert port.last_response.json()["form"] == {
        "creation_time": "2020-10-11 10:22:01",
        "ticket_id": "123",
    }
