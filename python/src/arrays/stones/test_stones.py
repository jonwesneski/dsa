from stones import stones

def test_stones_basic():
    # Since it's random, we can't assert a specific output unless we know the game is deterministic for specific inputs (it isn't here).
    # But for [2,2], it should always be 0.
    assert stones([2,2]) == 0

def test_stones_runs():
    # Just ensure it terminates and returns an int
    result = stones([2,7,4,1,8,1])
    assert isinstance(result, int)
    # 0 or 1 is likely result for [2,7,4,1,8,1]? 
    # Max possible result is 1. (8-7=1, 4-2=2, 2-1=1, 1-1=0 => 1)
    assert result >= 0
