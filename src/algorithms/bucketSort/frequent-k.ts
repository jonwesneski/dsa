/**
 * Problem: Top K Frequent Elements
 * Difficulty: Medium
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
export const topKFrequent = (nums: number[], k: number): number[] => {
  // Step 1: Count frequencies
  const frequencies: Record<number, number> = {};
  for (const num of nums) {
    frequencies[num] = (frequencies[num] || 0) + 1;
  }

  // Step 2: Bucket sort by frequency
  const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);
  for (const [numStr, freq] of Object.entries(frequencies)) {
    buckets[freq].push(parseInt(numStr));
  }

  // Step 3: Collect top k from highest frequency buckets
  const result: number[] = [];
  for (let freq = buckets.length - 1; freq >= 0 && result.length < k; freq--) {
    result.push(...buckets[freq]);
  }

  return result.slice(0, k);
};
