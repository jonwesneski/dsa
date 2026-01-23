from can_place_flowers import can_place_flowers

def test_can_place_flowers_basic():
    assert can_place_flowers([1,0,0,0,1], 1) == True

def test_can_place_flowers_fail():
    assert can_place_flowers([1,0,0,0,1], 2) == False

def test_can_place_flowers_edge():
    assert can_place_flowers([0,0,1,0,0], 1) == True
