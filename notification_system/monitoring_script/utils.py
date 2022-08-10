from functools import wraps

from sentry_sdk import capture_exception


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            capture_exception(err)
        else:
            return res
    return wrapper
