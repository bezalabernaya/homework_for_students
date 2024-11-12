from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    while obj:
        for i in obj:
            yield i

class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = obj

    def __iter__(self):
        while self.obj:
            for i in self.obj:
                yield i

    def __next__(self):
        return self

