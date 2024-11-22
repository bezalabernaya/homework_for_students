# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])

import time
from datetime import timedelta


def retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exception)] = Exception):
    if count < 1:
        raise ValueError

    def decorator(func):

        def catching_exceptions(*args, **kwargs):
            i = count
            while i > 0:
                i -= 1
                try:
                    return func(*args, **kwargs)
                except handled_exceptions:
                    if i == 0:
                        raise
                time.sleep(delay.total_seconds())

        return catching_exceptions
    return decorator
