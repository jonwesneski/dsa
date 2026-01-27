from picking_numbers import picking_numbers

def test_picking_numbers_basic():
    assert picking_numbers([4, 6, 5, 3, 3, 1]) == 3

def test_picking_numbers_mixed():
    assert picking_numbers([1, 2, 2, 3, 1, 2]) == 5

def test_picking_numbers_all_same():
    assert picking_numbers([66] * 100) == 100
