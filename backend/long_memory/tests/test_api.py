from hamcrest import assert_that, equal_to, has_key

from config import LOGIN, PASSWORD, EMAIl


def test_registration(long_memory_api):
    status_code, data = long_memory_api.registration(LOGIN, PASSWORD, EMAIl)
    assert_that(status_code, equal_to(201))
    assert_that(data, has_key('token'))


def test_authorization(long_memory_api):
    status_code, data = long_memory_api.authorization(LOGIN, PASSWORD)
    assert_that(status_code, equal_to(200))
    assert_that(data, has_key('token'))
