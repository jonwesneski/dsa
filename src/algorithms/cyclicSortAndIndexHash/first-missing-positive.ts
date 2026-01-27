/**
 * Problem: First Missing Positive
 * Difficulty: Hard
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
export const firstMissingPositive = (nums: number[]): number => {
  const n = nums.length;

  // Step 1: Place each number in its "correct" position
  // Number k should be at index k-1
  for (let i = 0; i < n; i++) {
    while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] !== nums[i]) {
      // Swap nums[i] to its target position
      const targetIdx = nums[i] - 1;
      [nums[i], nums[targetIdx]] = [nums[targetIdx], nums[i]];
    }
  }

  // Step 2: Find first index where nums[i] !== i + 1
  for (let i = 0; i < n; i++) {
    if (nums[i] !== i + 1) {
      return i + 1;
    }
  }

  // All positions filled correctly, answer is n + 1
  return n + 1;
};
