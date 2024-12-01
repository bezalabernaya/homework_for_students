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
        self._iter_idx1 = 0
        self._iter_idx2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_idx1 < len(self.iterables):
            if self._iter_idx2 < len(self.iterables[self._iter_idx1]):
                self._iter_idx2 += 1
            else:
                self._iter_idx2 = 1
                self._iter_idx1 += 1
        try:
            return self.iterables[self._iter_idx1][self._iter_idx2 - 1]
        except Exception:
            raise StopIteration


