
from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
import pytest


# Object-values
@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

class Money(NamedTuple):
    currency: str
    value: int

    def __add__(self, obj):
        if isinstance(obj, Money):
            if self.currency == obj.currency:
                return Money(self.currency, self.value + obj.value)
            raise ValueError
        raise TypeError

    def __sub__(self, obj):
        if isinstance(obj, Money):
            if self.currency == obj.currency:
                if self.value >= obj.value:
                    return Money(self.currency, self.value - obj.value)
                raise ValueError
            raise ValueError
        raise TypeError

    def __mul__(self, obj):
        if isinstance(obj, int):
            if obj != 0:
                return Money(self.currency, self.value * obj)
            raise ValueError
        raise TypeError

Line = namedtuple('Line', ['sku', 'qty'])

# Tests
fiver = Money('gbp', 5)
tenner = Money('gbp', 10)

def test_equality():
    assert Money('gdp', 5) == Money('gdp', 5)
    assert Name('Harry', 'Musk') != Name('Barry', 'Musk')
    assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)

def test_can_add():
    assert fiver + fiver == tenner

def test_can_sub():
    assert tenner - fiver == fiver

def test_add_different_currencies():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 10)

def test_can_multiply():
    with pytest.raises(TypeError):
        Money('gbp', 10) * Money('gbp', 10)

def test_can_multiply_by_number():
    assert fiver * 2 == tenner

def test_can_multiply_by_zero():
    with pytest.raises(ValueError):
        fiver * 0
