import pytest

@pytest.fixture(scope='function',autouse=True)
def post_uut():
    print('test starts')
    yield
    print('test finishes')