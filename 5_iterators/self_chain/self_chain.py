from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""

    for i in iterables:
        for j in i:
            yield j

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.iterables = iterables

    def __iter__(self):
        for i in self.iterables:
            for j in i:
                yield j

    def __next__(self):
        return self


