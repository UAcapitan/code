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