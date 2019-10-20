from unittest.mock import patch

from pytest import fixture

from lottery.lottery import lottery


@fixture(autouse=True, scope='module')
def mocked_open():
    with patch('lottery.lottery.open') as mock:
        yield mock


@fixture(autouse=True, scope='module')
def mocked_requests():
    with patch('lottery.lottery.requests') as mock:
        yield mock


@fixture(autouse=True, scope='module')
def mocked_randint():
    with patch('lottery.lottery.randint') as mock:
        mock.return_value = 546
        yield mock


def test_lottery(mocked_open, mocked_randint, mocked_requests):
    assert lottery() == {'ticket_no': 546}
    mocked_randint.assert_called_with(1, 1000)
    mocked_open.assert_called_with('ticket.log', 'a')
    mocked_open().__enter__().write.assert_called_with('546\n')
    mocked_requests.post.assert_called_with(
        'https://httpbin.org/post',
        data={'ticket_no': 546},
    )
