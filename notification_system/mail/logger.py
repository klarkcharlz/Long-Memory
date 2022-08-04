import sentry_sdk

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

"""
example
from sentry_sdk import capture_exception

try:
    a_potentially_failing_function()
except Exception as e:
    # Alternatively the argument can be omitted
    capture_exception(e)
"""