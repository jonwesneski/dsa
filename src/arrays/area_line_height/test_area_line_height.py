from area_line_height import area_line_height

def test_area_line_height_basic():
    # Example logic: if 'a' is 1, 'b' is 2... 
    # If heights is all 1s.
    heights = [1] * 26
    word = "abc"
    assert area_line_height(heights, word) == 3 # 3 * 1

def test_area_line_height_varied():
    heights = [1] * 26
    heights[0] = 5 # 'a' is 5
    word = "abc"
    assert area_line_height(heights, word) == 3 * 5 # tallest is 5, len is 3 -> 15
