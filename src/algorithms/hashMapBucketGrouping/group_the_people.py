"""
Problem: Group the People Given the Group Size They Belong To
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

def group_the_people(group_sizes: list[int]) -> list[list[int]]:
    groups = [[] for _ in range(len(group_sizes)+1)]
    filled_buckets = []
    
    # NOTE: The original Logic used buckets based on size.
    # Logic:
    # groups[size] is a list of indices.
    # If len(groups[size]) == size, flush it to filled_buckets.
    # NOTE: The original loop condition `if len(groups[groupSizes[i]]) == groupSizes[i]` checked BEFORE appending?
    # No, it appended `groups[groupSizes[i]].append(i)` in the ELSE block.
    # Wait, the original logic:
    # if len == size: flush, reset.
    # else: append.
    # This means if I have size 3, indices 0,1,2.
    # 0: append. (len 1)
    # 1: append. (len 2)
    # 2: append. (len 3)
    # 3: if len(3)==3? Yes. Flush. BUT we haven't appended the NEW one yet?
    # The original logic had:
    # if len == size: flush, THEN reset to `[i]`.
    # else: append.
    # This works. Steps:
    # 1. Check if current bucket full.
    # 2. If full, save it, start new bucket with current person.
    # 3. If not full, add current person.
    
    # Wait, if bucket is full, we flush it and start a NEW one with current person.
    # But what if specific group sizes are done?
    # Example: sizes [3,3,3,3,3,3].
    # i=0 (3): append. bucket3=[0]
    # i=1 (3): append. bucket3=[0,1]
    # i=2 (3): append. bucket3=[0,1,2] (NOW FULL)
    # i=3 (3): IS bucket3 full? yes (len 3). Flush [0,1,2]. Reset bucket3=[3].
    # i=4 (3): append. bucket3=[3,4]
    # i=i (3): append. bucket3=[3,4,5].
    # END Loop.
    # Return filled + remaining.
    # The remaining `[3,4,5]` is full, but strictly validation happens on NEXT iteration or return.
    # The return statement `filled_buckets + [x for x in groups if x]` handles the last buckets.
    # But wait, `groups` is size N+1. `groups[3]` is `[3,4,5]`.
    # The logic seems fine.
    
    for i in range(len(group_sizes)):
        size = group_sizes[i]
        if len(groups[size]) == size:
            filled_buckets.append(groups[size])
            groups[size] = [i]
        else:
            groups[size].append(i)
            
    return filled_buckets + [x for x in groups if x]
