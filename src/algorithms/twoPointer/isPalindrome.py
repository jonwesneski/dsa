def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome("Was it a car or a cat I saw?")) # True
print(isPalindrome("tab a cat")) # False
