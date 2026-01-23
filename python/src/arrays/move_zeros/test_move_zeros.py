from move_zeros import move_zeros

def test_move_zeros_basic():
    assert move_zeros([0,1,0,3,12]) == [1,3,12,0,0]

def test_move_zeros_none():
    assert move_zeros([0]) == [0]

def test_move_zeros_no_zeros():
    assert move_zeros([1,2,3]) == [1,2,3]
