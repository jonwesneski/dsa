## Idea

You are checking 2 items at the same time and then determining if you found the answer or if you need to move 1 of the 2 pointers. You can start the pointers on opposite ends of start them next to each other; it depends on the problem

### Opposite Ends

Used when:

- array is sorted
- you’re looking for pairs, ranges, or comparisons

```
arr = [1, 2, 4, 6, 8, 9]
L → start
R → end

Index:  0  1  2  3  4  5
Array: [1, 2, 4, 6, 8, 9]
        ↑              ↑
        L              R

1 + 9 = 10  (too small → move L)
[1, 2, 4, 6, 8, 9]
    ↑           ↑
    L           R

OR (depending on the problem)

1 + 9 = 10  (too large → move R)
[1, 2, 4, 6, 8, 9]
    ↑        ↑
    L        R
```

#### psuedo code

```
left = 0
right = n - 1

while left < right:
    if condition_met:
        return true
    else if need_bigger:
        left += 1
    else:
        right -= 1
```

### Same direction (sliding window style)

Used when:

- subarrays / substrings
- contiguous ranges
- max/min window problems

```
arr = [2, 1, 3, 2, 1]
L → start
R → start

Index:  0  1  2  3  4
Array: [2, 1, 3, 2, 1]
        ↑
        L,R

2 + 2 = 4  (too small → move R)
[2, 1, 3, 2, 1]
↑   ↑
L   R

OR

2 + 1 = 3  (too large → move L)
[2, 1, 3, 2, 1]
    ↑        ↑
    L        R
```

#### psuedo code

```
left = 0
current = 0

for right in range(0, n):
    current += arr[right]

    while constraint_broken:
        current -= arr[left]
        left += 1

    update_answer()
```

## Fast & Slow Pointer

Used when:

- linked lists
- cycle detection
- removing duplicates
- in-place array modifications

```
arr = [1, 1, 2, 2, 3]
slow = 0
fast = 1

[1, 1, 2, 2, 3]
 ↑  ↑
 S  F

On 1st iteration:
arr[fast] == arr[slow] → skip

[1, 1, 2, 2, 3]
 ↑     ↑
 S     F
```

#### psuedo code

```
slow = 0

for fast in range(1, n):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
```

## When you SHOULD use two pointers

✅ Data is sorted

✅ You’re dealing with pairs or ranges

✅ Problem mentions:

- “subarray”
- “substring”
- “remove duplicates”
- “in-place”
- “find pair with sum…”
- “longest/shortest window”
- “contiguous”

## When you should NOT use it

❌ Data is unsorted and order matters (unless you sort)

❌ You need all combinations

❌ Random access jumps (trees, graphs)

❌ Non-monotonic constraints (sum goes up/down unpredictably)
