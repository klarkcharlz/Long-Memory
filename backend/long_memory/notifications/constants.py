from dateutil.relativedelta import relativedelta


TIME_DELTA_MAP = {
    0: relativedelta(days=1),
    1: relativedelta(days=3),
    2: relativedelta(weeks=1),
    3: relativedelta(weeks=3),
    4: relativedelta(months=1),
    5: relativedelta(months=3),
    6: relativedelta(months=6),
}
