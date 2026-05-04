import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_sum(numbers):
    result = sum(numbers)
    assert result == 15


def test_count(numbers):
    result = len(numbers)
    assert result == 5
