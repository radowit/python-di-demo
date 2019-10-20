from random import Random
from tempfile import mkstemp

from pytest import mark

from lottery.ports import APIPort, FilePort, RandomPort


def test_random_port():
    port = RandomPort(Random(10000), 1000)

    assert port.generate() == 592


@mark.integration
def test_file_port():
    __, path = mkstemp()
    port = FilePort(path)

    port.save(123)
    port.save(987)

    with open(path, "r") as desc:
        assert desc.read() == "123\n987\n"


@mark.integration
def test_api_port():
    port = APIPort("https://httpbin.org/post")

    port.send(123)

    assert port.last_response.status_code == 200
    assert port.last_response.json()["form"] == {"ticket_no": "123"}
