from minimum_operations_to_write_y import minimum_operations_to_write_y

def test_min_ops_basic():
    grid = [[1,2,2],[1,1,0],[0,1,0]]
    assert minimum_operations_to_write_y(grid) == 3

def test_min_ops_complex():
    grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
    assert minimum_operations_to_write_y(grid) == 12
