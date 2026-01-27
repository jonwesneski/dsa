/**
 * Problem: Two Sum
 * Difficulty: Easy
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
export const twoSum = (nums: number[], target: number) => {
  const hashmap: Record<number, number> = {};

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (diff in hashmap) {
      return [hashmap[diff], i];
    }
    hashmap[nums[i]] = i;
  }
  return [-1, -1];
};
