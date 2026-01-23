from group_the_people import group_the_people

def test_group_the_people_basic():
    # Input: [3,3,3,3,3,1,3]
    # Output: [[5], [0,1,2], [3,4,6]] (Order of groups might vary, order within groups too)
    # My refactor preserves order.
    result = group_the_people([3,3,3,3,3,1,3])
    # Expected: 
    # grp 1: [5]
    # grp 3: [0,1,2] then [3,4,6]
    # Length check
    assert len(result) == 3
    
    # Check contents
    # Sort groups by first element to check deterministically if needed
    # But simple logic check:
    flattened = [item for sublist in result for item in sublist]
    assert sorted(flattened) == [0,1,2,3,4,5,6] # All people accounted for
    
    for group in result:
        size = len(group)
        # Check if the people in this group actually asked for this size
        for person in group:
            # We need the original input to verify, but we can hardcode for this test
            expected_size = 1 if person == 5 else 3
            assert size == expected_size
