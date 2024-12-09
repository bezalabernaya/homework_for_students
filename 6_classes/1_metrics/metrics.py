import datetime
from dateutil import tz
from typing import Protocol


class Statsd:
    def __init__(self, path, buffer_limit, sep, start):
        """Реализуйте класс"""
        self.buffer = []
        self.data = datetime.datetime.now(tz=tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%S%z")
        self.path = path
        self.buffer_limit = buffer_limit
        self.sep = sep
        self.start = start
        self._file = None

    def __enter__(self):
        self._file = open(self.path,'a')
        return self._file

    def __exit__(self, type, value, traceback):
        if self._file is not None:
            self._file.close()
        return True

    def incr(self, name: str):
        self.buffer.append(f"{self.data}{self.sep}{name}{self.sep}1")
        if len(self.buffer) == self.buffer_limit:
            Writer().write_metrics(filepath=self.path, b=self.buffer, start=self.start)
            self.buffer.clear()

    def decr(self, name: str):
        self.buffer.append(f"{self.data}{self.sep}{name}{self.sep}-1")
        if len(self.buffer) == self.buffer_limit:
            Writer().write_metrics(filepath=self.path, b=self.buffer, start=self.start)
            self.buffer.clear()



'''class CSVWriter:
    def write_metrics(self, filepath: str):
        metrics = []
        with open(filepath, "r") as file:
            reader = csv.reader(file, delimiter=";")
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue

                metrics.append(Metric(*row))

        return metrics'''


class Writer:

    def write_metrics(self, filepath: str, b, start):
        try:
            with open(filepath, "r") as file:
                line = file.readlines()
            if start in line:
                with open(filepath, "a") as file:
                    for line in b:
                        file.write(line + '\n')
        except Exception:
            with open(filepath, "a") as file:
                if start:
                    file.write(start)
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

if __name__ == '__main__':
    statsd = get_txt_statsd("metrics.txt")
    for i in range(20):
        statsd.incr('giu')

