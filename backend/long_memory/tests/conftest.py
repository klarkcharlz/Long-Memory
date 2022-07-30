import pytest

from framework.long_memory_api import LongMemoryAPI
from config import HOST


@pytest.fixture(scope='session')
def long_memory_api():
    return LongMemoryAPI(host=HOST)
