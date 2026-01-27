"""
Problem: Last Stone Weight (Randomized Variant?)
Difficulty: Medium
Time Complexity: Unbounded (Randomized) - Warning: Inefficient logic
Space Complexity: O(N)
"""
import random

def stones(stones: list[int]) -> int:
    destroyed_indices = {i : False for i in range(len(stones))}
    last_index = len(stones) - 1
    # Check if we have more than 1 active stone
    # The logic provided by user was `while len(destroyed_indices.keys()) != 1:`
    # But destroyed_indices is just a map, it doesn't shrink in the original loop condition logic properly since keys() returns all keys.
    # Wait, the user logic has `del destroyed_indices[random_index1]`. So keys() size DOES change.
    
    while len(destroyed_indices.keys()) > 1:
        # Note: The user loop condition was `!= 1`. If it goes to 0 (if stones destroy each other fully?), it might crash or loop forever.
        # But let's assume valid inputs.
        
        # Need to handle case where no indices left or valid random pick logic.
        # The user has `while stones[random_index1] == 0`.
        # This implementation requires existing stones to be non-zero? 
        # But if `stones` array is mutated to 0, and we seek non-zero, that's fine.
        
        # Safety check to prevent infinite loop in tests if logic is flawed
        valid_indices = [i for i in destroyed_indices.keys()]
        if len(valid_indices) < 2:
            break

        random_index1 = random.choice(valid_indices)
        random_index2 = random.choice(valid_indices)
        
        while random_index1 == random_index2:
             random_index2 = random.choice(valid_indices)
        
        # NOTE: The user's original logic was doing random selection on indices 0..last_index and checking if they were 0 or deleted.
        # My `random.choice(valid_indices)` is safer and faster.
        # However, to preserve "exact" logic I should match the user's potentially slow approach?
        # No, "Improvements" allows me to make it functional. Random choice from valid keys is semantically similar but optimized.
        
        val1 = stones[random_index1]
        val2 = stones[random_index2]
        
        if val1 == val2:
            del destroyed_indices[random_index1]
            del destroyed_indices[random_index2]
            stones[random_index1] = 0
            stones[random_index2] = 0
        elif val1 > val2:
            stones[random_index1] = val1 - val2
            del destroyed_indices[random_index2]
            stones[random_index2] = 0
        else:
            del destroyed_indices[random_index1]
            stones[random_index1] = 0
            stones[random_index2] = val2 - val1
            
    if not destroyed_indices:
        return 0 # All destroyed?
    return stones[list(destroyed_indices.keys())[0]]
