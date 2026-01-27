from intersect import intersect
from collections import Counter

def test_intersect_basic():
    result = intersect([1,2,2,1], [2,2])
    # Order doesn't strictly matter for intersection usually, but the implementation returns a list.
    # We should sort or check counts to be robust.
    assert sorted(result) == sorted([2,2])

def test_intersect_complex():
    result = intersect([4,9,5], [9,4,9,8,4])
    assert sorted(result) == sorted([4,9])
