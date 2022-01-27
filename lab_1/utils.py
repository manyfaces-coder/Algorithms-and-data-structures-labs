import time


def time_track(func) -> object:
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 9)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)')
        return result
    return surrogate