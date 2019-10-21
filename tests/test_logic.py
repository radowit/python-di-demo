from unittest.mock import Mock

from pytest import fixture

from lottery.logic import TicketGenerator, TicketSaver
from lottery.ports import APIPort, FilePort, RandomPort


@fixture
def dummy_random():
    return Mock(RandomPort, generate=Mock(return_value=527))


@fixture
def dummy_api():
    return Mock(APIPort)


@fixture
def dummy_file():
    return Mock(FilePort)


def test_generate_ticket(dummy_random):
    logic = TicketGenerator(random_port=dummy_random)

    assert logic.generate_ticket().ticket_id == 527


def test_send(dummy_api, dummy_file):
    logic = TicketSaver(api_port=dummy_api, file_port=dummy_file)

    logic.save_ticket(527)

    dummy_api.send.assert_called_with(527)
    dummy_file.save.assert_called_with(527)
