class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


persons = [
    Person('Суворов', 52, "полководец"),
Person('Рахманинов', 50, "пианист"),
Person('Балакирев', 34, "программист"),
]