/**
 * Problem: First Missing Positive
 * Difficulty: Hard
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
export const firstMissingPositive = (nums: number[]) => {
  let current = 1;
  nums.sort((a, b) => a - b);
  // console.log(nums);
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= 0 || nums[i - 1] === nums[i]) {
      continue;
    }
    if (nums[i] !== current) {
      break;
    }
    current++;
  }
  return current;
};
