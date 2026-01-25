================================================================================

1. # FIXED SIZE SLIDING WINDOW
   Problem: Find maximum sum of any subarray of size k

```
function maxSumFixedWindow(arr, k):
    n = length of arr
    if n < k:
    return error "Array too small"

    // Calculate sum of first window
    windowSum = 0
    for i from 0 to k-1:
        windowSum += arr[i]

    maxSum = windowSum

    // Slide the window: add next element, remove first element
    for i from k to n-1:
        windowSum = windowSum + arr[i] - arr[i - k]  // O(1) slide operation
        maxSum = max(maxSum, windowSum)

    return maxSum
```

// Example: arr = [2, 1, 5, 1, 3, 2], k = 3
// Window 1: [2, 1, 5] → sum = 8
// Window 2: [1, 5, 1] → sum = 7 (add 1, remove 2)
// Window 3: [5, 1, 3] → sum = 9 (add 3, remove 1)
// Window 4: [1, 3, 2] → sum = 6 (add 2, remove 5)
// Result: 9

```
function alternateMaxSumFixedWindow(arr, k):

    windowSum = 0
    maxSum = -infinity
    for i from 0 to arr.length:
        windowSum += arr[i]
        // Only check maxSum if we are at k or greater
        // all other iterations (smaller than k; it is building the window)
        if (i >= k - 1)
           maxSum = max(maxSum, windowsum)
           // subtract the windowStart/Left from sum for next iteration
           windowSum -= arr[i-(k-1)]
    return maxSum
```

# ================================================================================ 2. DYNAMIC (VARIABLE SIZE) SLIDING WINDOW

Problem: Find longest substring with at most k distinct characters

```
function longestSubstringKDistinct(s, k):
    left = 0
    maxLength = 0
    charCount = new Map() // Track character frequencies

    // Expand window with right pointer
    for right from 0 to length(s) - 1:
        // Add current character to window
        char = s[right]
        charCount[char] = charCount.get(char, 0) + 1

        // Shrink window from left while constraint violated
        while number of distinct chars in charCount > k:
            leftChar = s[left]
            charCount[leftChar] -= 1

            if charCount[leftChar] == 0:
                remove leftChar from charCount

            left += 1  // Shrink window

        // Update result with valid window size
        maxLength = max(maxLength, right - left + 1)

    return maxLength
```

// Example: s = "eceba", k = 2
// Window expands: e, ec, ece (valid - 2 distinct)
// Window expands: eceb (invalid - 3 distinct)
// → Shrink: ceb (valid - 2 distinct)
// Window expands: ceba (invalid - 3 distinct)
// → Shrink: eba (valid - 2 distinct)
// Result: 3 (length of "ece" or "ceb")

# ================================================================================ 3. DYNAMIC WINDOW WITH AUXILIARY DATA STRUCTURE

Problem: Find minimum window substring containing all characters of pattern

```
function minWindowSubstring(s, pattern):
    left = 0
    minLength = infinity
    minStart = 0

    // Auxiliary data structures
    required = new Map()  // Characters needed from pattern
    windowCounts = new Map()  // Characters in current window

    // Build requirement map
    for char in pattern:
        required[char] = required.get(char, 0) + 1

    requiredChars = size of required
    formed = 0  // Count of unique chars that meet requirement

    for right from 0 to length(s) - 1:
        // Expand: add character to window
        char = s[right]
        windowCounts[char] = windowCounts.get(char, 0) + 1

        // Check if current character's frequency matches requirement
        if char in required AND windowCounts[char] == required[char]:
            formed += 1

        // Contract: try to minimize window while maintaining validity
        while formed == requiredChars AND left <= right:
            // Update result if this window is smaller
            windowLength = right - left + 1
            if windowLength < minLength:
                minLength = windowLength
                minStart = left

            // Remove leftmost character
            leftChar = s[left]
            windowCounts[leftChar] -= 1

            // Check if removing this breaks the requirement
            if leftChar in required AND windowCounts[leftChar] < required[leftChar]:
                formed -= 1

            left += 1  // Shrink window

    if minLength == infinity:
        return ""

    return s.substring(minStart, minStart + minLength)
```

// Example: s = "ADOBECODEBANC", pattern = "ABC"
// Window expands until all chars found: "ADOBEC" (has A, B, C)
// Window shrinks: "DOBEC" (still has A, B, C? No - missing A)
// Continue expanding: "ODEBANC" (has A, B, C)
// Window shrinks: "BANC" (minimal valid window)
// Result: "BANC"

================================================================================
KEY DIFFERENCES SUMMARY
================================================================================

Fixed Window:

- Window size is constant (k)
- Simple slide: add one element, remove one element
- Two pointers move together (right = left + k)
- Time: O(n), Space: O(1)

Dynamic Window:

- Window size changes based on constraint
- Right pointer expands, left pointer contracts when needed
- Both pointers move independently
- Time: O(n), Space: O(k) where k is unique elements in window

Dynamic with Auxiliary Structure:

- Complex constraints requiring tracking of multiple conditions
- Uses hash maps, deques, or other structures
- More sophisticated validity checking
- Time: O(n), Space: O(m) where m is pattern/constraint size

================================================================================
WHEN TO USE EACH TECHNIQUE
================================================================================

Fixed Window:

- "Find max/min of all subarrays of size k"
- "Average of all subarrays of length k"
- Window size is explicitly given

Dynamic Window:

- "Longest/shortest subarray with sum ≤ k"
- "Subarray with at most k distinct elements"
- Constraint is on window properties, not size

Dynamic with Auxiliary:

- "Minimum window containing all characters"
- "Longest substring without repeating characters"
- "Subarrays with exactly k different integers"
- Need to track complex state (frequencies, order, etc.)
