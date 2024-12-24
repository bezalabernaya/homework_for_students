import datetime
import csv


class Statsd:
    def __init__(self, writer, buffer_limit):
        """Реализуйте класс"""
        self.buffer_limit = buffer_limit
        self._buffer = []
        self.writer = writer
        self.writer.create_file()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.writer.write_metrics(self._buffer)
        return False

    def incr(self, name: str):
        date = datetime.datetime.now(datetime.UTC)
        value = 1
        self._buffer.append([date.strftime("%Y-%m-%dT%H:%M:%S%z"), name, str(value)])
        if len(self._buffer) >= self.buffer_limit:
            self.writer.write_metrics(self._buffer)
            self._buffer.clear()

    def decr(self, name: str):
        date = datetime.datetime.now(datetime.UTC)
        value = -1
        self._buffer.append([date.strftime("%Y-%m-%dT%H:%M:%S%z"), name, str(value)])
        if len(self._buffer) >= self.buffer_limit:
            self.writer.write_metrics(self._buffer)
            self._buffer.clear()


class WriterTXT:
    def __init__(self, path):
        self._path = path

    def create_file(self):
        with open(self._path, "w") as file:
            pass

    def write_metrics(self, buffer):
        with open(self._path, "a") as file:
            for line in buffer:
                file.write(f'{line[0]} {line[1]} {line[2]}\n')


class WriterCSV:
    def __init__(self, path):
        self._path = path

    def create_file(self):
        with open(self._path, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
            writer.writerow(["date", "metric", "value"])

    def write_metrics(self, buffer):
        with open(self._path, "a") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
            for line in buffer:
                writer.writerow(line)


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    if path.endswith('.txt'):
        writer = WriterTXT(path=path)
        return Statsd(writer, buffer_limit)
    else:
        raise ValueError


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    if path.endswith('.csv'):
        writer = WriterCSV(path=path)
        return Statsd(writer, buffer_limit)
    else:
        raise ValueError



