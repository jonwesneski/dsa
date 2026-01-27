/**
 * Problem: Top K Frequent Elements
 * Difficulty: Medium
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
export const frequentK = (nums: number[], k: number) => {
  const frequencies: Record<number, number> = {};
  for (const num of nums) {
    if (num in frequencies) {
      frequencies[num] += 1;
    } else {
      frequencies[num] = 1;
    }
  }

  // Note: The original implementation filters but map keys are strings?
  // Object.entries returns [string, number].
  // entry[0] is string. We should parseInt it if we return numbers.
  // The original returns `entry[0]`, which is string.
  // BUT the function signature `number[]` was implied? or any?
  // Let's coerce to number to be safe/correct.
  
  return Object.entries(frequencies)
    .filter((entry) => entry[1] >= k)
    .map((entry) => parseInt(entry[0]));
};
