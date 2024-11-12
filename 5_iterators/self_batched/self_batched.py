from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""

    for i in range(0, len(obj), n):
        if len(obj) - i < n:
            yield tuple(obj[i:])
        else:
            yield tuple(obj[i:i + n])


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        """Реализуй этот класс."""
        self.obj = obj
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.obj):
            if len(self.obj) - self.counter < self.n:
                batch = tuple(self.obj[self.counter:])
            else:
                batch = tuple(self.obj[self.counter: self.counter + self.n])
            self.counter += self.n
            return batch

        else:
            raise StopIteration

