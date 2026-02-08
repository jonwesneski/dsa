## Idea

Mainly used for searching a monotonic decision space, meaning data only moves in one direction (only increases or decreases). On a sorted array you can cut your problem subset in half on each iteration eventually finding the solution. A good example is trying to flip to a certain page in a book. We are instructed to turn to page 400, we are not sure how many pages there are so we start in the middle. If that page is less than 400 then we take the middle and the end of the book; cutting our search in half and find the middle again. if that is still less than 400 then we repeat the process. Or if it is greater than look the the left half of that chunk

```
nums = [1, 3, 5, 7, 9, 11]
target = 7


[1, 3, 5, 7, 9, 11]
 L     M         R

ITERATION 1
nums[M] = 5 < 7
→ discard left half

ITERATION 2
[7, 9, 11]
 L  M   R
 nums[M] = 9 > 7
 → discard right half

ITERATION 3
[7]
 L/M/R
found
```

When you SHOULD use binary search

✅ Data is sorted

✅ You can define a monotonic condition

✅ You’re looking for:

- first / last
- minimum / maximum
- boundary
- smallest value that works

Interview keyword triggers:

- “minimum”
- “maximum”
- “at least”
- “at most”
- “first time”
- “last time”

When you should NOT use it:
❌ Data is unsorted AND order matters

❌ Condition flips multiple times

❌ You need all matches

❌ Graph / tree traversal problems

❌ Answer space is not monotonic

Common binary search mistakes:
🚫 Infinite loops

🚫 Off-by-one errors

🚫 Wrong loop condition (< vs <=)

🚫 Updating the wrong boundary

🚫 Searching values instead of conditions
