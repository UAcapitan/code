
def test_vector():
    v1 = Vector(2, 5)
    v2 = Vector(2, 2)

    assert v1 + v2 == Vector(4, 7)
