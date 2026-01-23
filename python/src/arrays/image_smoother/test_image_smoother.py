from image_smoother import image_smoother

def test_image_smoother_3x3_ones():
    input_grid = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[0,0,0],[0,0,0],[0,0,0]] 
    # Wait, the logic average of 1s and 0 should NOT be 0? 
    # (1*8 + 0)/9 = 8/9 = 0 (floor). Correct.
    assert image_smoother(input_grid) == expected

def test_image_smoother_large():
    input_grid = [[100,200,100],[200,50,200],[100,200,100]]
    expected = [[137,141,137],[141,138,141],[137,141,137]]
    assert image_smoother(input_grid) == expected

def test_image_smoother_varied():
    input_grid = [[100, 0, 10], [0, 0, 25], [10, 10, 10]]
    expected = [[25, 22, 8], [20, 18, 9], [5, 9, 11]]
    assert image_smoother(input_grid) == expected
