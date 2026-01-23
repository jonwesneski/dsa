from rotate_array import rotate_array

def test_rotate_array_basic():
    assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

def test_rotate_array_full_rotation():
    assert rotate_array([1, 2], 2) == [1, 2]

def test_rotate_array_large_k():
    assert rotate_array([1, 2], 3) == [2, 1]
