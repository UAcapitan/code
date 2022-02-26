from app import *

class TestsOfApp:
    def test_answer(self):
        assert inc(1) == 2

    def test_inc_type(self):
        assert type(inc(1)) == int