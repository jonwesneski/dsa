from two_sum import two_sum

def test_two_sum_basic():
    result = two_sum([2,7,11,15], 9)
    assert result == [0, 1] or result == [1, 0]

def test_two_sum_none():
    assert two_sum([1,2], 10) == [-1, -1]
