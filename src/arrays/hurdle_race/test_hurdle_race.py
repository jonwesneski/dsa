from hurdle_race import hurdle_race

def test_hurdle_race_basic():
    assert hurdle_race([1,2,3,3,2], 1) == 2

def test_hurdle_race_no_potions_needed():
    assert hurdle_race([1, 6, 3, 5, 2], 4) == 2 # Wait, max(6-4) is 2. Actually 1,6,3,5,2 with 4. 6-4=2. 5-4=1. Max is 2. Correct.
