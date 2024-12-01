import datetime
from dateutil import tz
import time
class Statsd:
    def __init__(self, path, buffer_limit, sep):
        """Реализуйте класс"""
        self.buffer = []
        self.data = datetime.datetime.now(tz=tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%S%z")
        self.path = path
        self.buffer_limit = buffer_limit
        self.sep = sep

    def send_buf(self, buffer):
        with open(self.path, 'w') as ouf:
            for _ in buffer:
                ouf.write(_ + '\n')

    def incr(self, name: str):
        self.buffer.append(f"{self.data}{self.sep}{name}{self.sep}1")
        if len(self.buffer) == self.buffer_limit:
            self.send_buf(buffer=self.buffer)
            self.buffer.clear()

    def decr(self, name: str):
        self.buffer.append(f"{self.data}{self.sep}{name}{self.sep}-1")
        if len(self.buffer) == self.buffer_limit:
            self.send_buf(self.buffer)
            self.buffer.clear()




def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    sep = ' '
    return Statsd(path, buffer_limit, sep)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    sep = ';'
    return Statsd(path, buffer_limit, sep)

'''if __name__ == '__main__':
    statsd = get_txt_statsd("metrics.txt")
    # statsd = get_csv_statsd("./path/to/metrics.csv")

    for _ in range(11):
        statsd.incr("auth_service.create_user.success")
        time.sleep(1)'''
