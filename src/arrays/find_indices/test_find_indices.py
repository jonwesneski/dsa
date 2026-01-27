from find_indices import find_indices

def test_find_indices_basic():
    # [2,7,9,11], 18 -> 7+11=18 (indices 1 and 3)
    # Wait, the code logic:
    # i=0, val=2, diff=16. Dict{2:0}
    # i=1, val=7, diff=11. Dict{2:0, 7:1}
    # i=2, val=9, diff=9. Dict{2:0, 7:1, 9:2}
    # i=3, val=11, diff=7. 7 in dict? Yes (index 1). Return (1, 3).
    assert find_indices([2,7,9,11], 18) == (1, 3)

def test_find_indices_none():
    assert find_indices([1, 2], 10) == (-1, -1)
