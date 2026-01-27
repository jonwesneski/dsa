from min_add_to_make_valid import min_add_to_make_valid

def test_min_add_basic():
    assert min_add_to_make_valid("())") == 1

def test_min_add_balanced():
    assert min_add_to_make_valid("((()))") == 0

def test_min_add_complex():
    assert min_add_to_make_valid("()))((") == 4
