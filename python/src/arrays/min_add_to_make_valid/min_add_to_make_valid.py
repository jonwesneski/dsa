"""
Problem: Minimum Add to Make Parentheses Valid
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

def min_add_to_make_valid(s: str) -> int:
    # Original logic used a map {"(": 0, ")": 0}.
    # Logic:
    # if '(', countMap['(']++
    # if ')': if countMap['(']>0, countMap['(']--. ELSE countMap[')']++
    # Return sum.
    # This logic correctly tracks open/close balance.
    
    open_needed = 0  # Represents countMap["("] relative to unpaired closes? 
    # Actually the user logic used keys "(" and ")" to store UNMATCHED ones?
    # Let's clean it up to variables.
    
    left_needed = 0 # '(' needed
    right_needed = 0 # ')' needed
    
    # Original implementation:
    # countMap = {"(": 0, ")": 0}
    # for ss in s:
    #     if countMap["("] > 0 and ss == ")":
    #         countMap["("] -= 1
    #     elif countMap["("] <= 0 and ss == ")":
    #         countMap[")"] += 1
    #     elif ss == "(":
    #         countMap["("] += 1
    # return countMap["("] + countMap[")"]
    
    # Cleaned:
    open_brackets = 0
    close_needed = 0
    
    for char in s:
        if char == '(':
            open_brackets += 1
        elif char == ')':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                close_needed += 1
    return open_brackets + close_needed
