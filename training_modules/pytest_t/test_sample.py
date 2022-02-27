import pytest
from app import *

class TestsOfApp:
    def test_answer(self):
        assert inc(1) == 2
        assert inc(7) == 8
        assert inc(55) == 56
        assert inc(11111) == 11112
        assert inc(15555555555554) == 15555555555555

    def test_inc_type(self):
        assert type(inc(1)) == int
        assert type(inc(55)) == int
        assert type(inc(57.0)) == int

    def test_error(self):
        with pytest.raises(Exception):
            error()

    def test_cap(self):
        assert cap('text') == 'Text'
        assert cap('start') == 'Start'
        assert cap('Zero') == 'Zero'

    def test_error_cap(self):
        with pytest.raises(AttributeError):
            cap(123.0)

    def test_some_errors(self):
        with pytest.raises(Exception):
            some_errors(10)
            some_errors(105.0)
            some_errors('110')

    def test_for_return_num(self):
        assert return_num(1) == 0
        assert return_num(5) == 0
        assert return_num(25) == 25

    def test_for_error_return_num(self):
        with pytest.raises(Exception):
            return_num(12)
            return_num(15)
            return_num(17)

class TestsForCalculator:
    def test_for_calculator(self):
        calculator = Calculator(10)
        calculator.add(10)
        assert calculator.get_n() == 20
        calculator.add(10)
        assert calculator.get_n() == 30
        calculator.add(0)
        assert calculator.get_n() == 30

        calculator.minus(0)
        assert calculator.get_n() == 30
        calculator.minus(10)
        assert calculator.get_n() == 20
        calculator.minus(17)
        assert calculator.get_n() == 3

        calculator.invert()
        assert calculator.get_n() == -3
        calculator.invert()
        assert calculator.get_n() == 3

        calculator.sqrt()
        assert calculator.get_n() == 9
    
    def test_for_types(self):
        with pytest.raises(Exception):
            Calculator('10')
            Calculator('abc')
            Calculator(123.1)
            Calculator([])
            Calculator(1,2,3)