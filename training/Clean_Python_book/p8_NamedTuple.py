
from typing import NamedTuple


class Car(NamedTuple):
    color: str
    distance: float
    auto_gear: bool

print(Car("black", 230_875.91, True))
