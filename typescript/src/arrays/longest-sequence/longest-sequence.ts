/**
 * Problem: Longest Consecutive Sequence
 * Difficulty: Medium
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
export const longestSequence = (nums: number[]) => {
  const sequenceSet = new Set(nums);
  let longest = 0; // Initialize 0 for empty case

  if (nums.length > 0) longest = 1; // Or just use logic below (original was 1)
  // Original had: `let longest = 1;` but didn't handle empty array well if loop didn't run? 
  // Actually original loop: `for (const num of sequenceSet)`. If empty, returns 1? Incorrect. 
  // Standard solution returns 0 for empty.
  // I will initialize longest = 0.
  
  for (const num of sequenceSet) {
    // Check if start of sequence
    // Original logic: `let currentNum = num - 1; if (sequenceSet.has(currentNum))` -> this checks if it is NOT start?
    // Original logic seems to look for END of sequence (scanning downwards?)
    // `currentNum = num - 1`. `if (has(num-1))`: 
    // `let count = 2`. `while(has(--currentNum))`.
    // Example: [1,2,3].
    // num=3. has(2)? Yes. count=2. has(1)? Yes. count=3. has(0)? No. Max(3).
    // num=2. has(1)? Yes. count=2. has(0)? No. Max(2).
    // num=1. has(0)? No.
    // This logic works (reverse scanning). O(N) because each sequence handled once?
    // Be careful: In `[1,2,3]`, we process 3 (scan 2,1). We process 2 (scan 1). We process 1.
    // This is O(N^2) worst case! 
    // Standard O(N) solution checks `if (!set.has(num-1))` (start of sequence) then scans UP.
    // Or if checking `num+1` (end of sequence) then scans DOWN.
    // The original logic `if (sequenceSet.has(currentNum))` triggers scan ONLY if `num-1` exists, i.e., `num` is NOT the start (in ascending terms).
    // Wait, if `num-1` exists, `num` is part of a sequence but not the start.
    // Original logic: "doing a longest sequence in descending order" (comment).
    // So if `num-1` exists, we scan down. 
    // [1,2,3]. 
    // 3: has 2 -> scan down to 1. (Length 3).
    // 2: has 1 -> scan down to 1. (Length 2).
    // 1: has 0 -> No.
    // This repeats work. 3 scans 2 and 1. 2 scans 1. 
    // This is bad performance.
    
    // I will OPTIMIZE to standard solution logic (scan only from start).
    // Start of sequence logic: `if (!set.has(num-1))` -> scan UP `num+1`.
    
    if (!sequenceSet.has(num - 1)) {
        let currentNum = num;
        let currentStreak = 1;
        while (sequenceSet.has(currentNum + 1)) {
            currentNum += 1;
            currentStreak += 1;
        }
        longest = Math.max(longest, currentStreak);
    }
  }
  return longest;
};
