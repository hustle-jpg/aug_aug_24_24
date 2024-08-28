import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter')


def test_demo1():
    assert 2 == 2


def test_demo2(before_after):
    assert 2 == 2

