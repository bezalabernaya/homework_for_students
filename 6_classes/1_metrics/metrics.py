import datetime
from dateutil import tz


class Statsd:
    def __init__(self, path, buffer_limit, sep, start):
        """Реализуйте класс"""
        self.path = path
        self.buffer_limit = buffer_limit
        self.sep = sep
        self._buffer = []
        self.writer = Writer()
        self.writer.check_header(filepath=self.path, start=start)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.writer.write_metrics(filepath=self.path, b=self._buffer)
        return False

    def incr(self, name: str):
        _data = datetime.datetime.now(tz=tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%S%z")
        self._buffer.append(f"{_data}{self.sep}{name}{self.sep}1")
        if len(self._buffer) == self.buffer_limit:
            self.writer.write_metrics(filepath=self.path, b=self._buffer)
            self._buffer.clear()

    def decr(self, name: str):
        _data = datetime.datetime.now(tz=tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%S%z")
        self._buffer.append(f"{_data}{self.sep}{name}{self.sep}-1")
        if len(self._buffer) == self.buffer_limit:
            self.writer.write_metrics(filepath=self.path, b=self._buffer)
            self._buffer.clear()


class Writer:

    def check_header(self, start, filepath):
        try:
            file = open(filepath, "r")
            line = file.readlines()
            if line != start:
                raise
        except Exception:
            file = open(filepath, "w")
            file.write(start)
        finally:
            file.close()

    def write_metrics(self, filepath: str, b, ):
        with open(filepath, "a") as file:
            for line in b:
                file.write(line + '\n')


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    if path.endswith('.txt'):
        return Statsd(path, buffer_limit, sep=' ', start='')
    else:
        raise ValueError


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    if path.endswith('.csv'):
        return Statsd(path, buffer_limit, sep=';', start='date;metric;value\n')
    else:
        raise ValueError




