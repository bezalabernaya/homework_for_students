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
        self._iter_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_idx >= len(self.obj):
            self._iter_idx = 0
        try:
            res = list(self.obj.keys())[self._iter_idx]
        except AttributeError:
            try:
                res = self.obj[self._iter_idx]
            except TypeError:
                res = list(self.obj)[self._iter_idx]
        finally:
            self._iter_idx += 1
        return res



