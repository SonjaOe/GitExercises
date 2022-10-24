class Person:
    def __init__(self, name: str, age: int):
        self._age = age
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, x):
        self._name = x
    def get_age(self):
        return self._age
    def set_age(self, y):
        self._age = y
    def __str__(self):
        return self._name