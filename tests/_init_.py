import src.math_operations as math_ops

def test_add():
    assert math_ops.add(2, 3) == 5
    assert math_ops.add(-1, 1) == 0
    assert math_ops.add(0, 0) == 0
    assert math_ops.add(-1, -1) == -2

def test_sub():
    assert math_ops.sub(5, 3) == 2
    assert math_ops.sub(0, 0) == 0
    assert math_ops.sub(-1, -1) == 0
    assert math_ops.sub(-1, 1) == -2