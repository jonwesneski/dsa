/**
 * Problem: Majority Element
 * Difficulty: Easy
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
export const majorityElement = (nums: number[]) => {
  // using hashmap
  // let result: Record<number, number> = {}
  // const majority = nums.length / 2
  // for (let i = 0; i < majority; i++) {
  //     const left = nums[i]
  //     const right = nums[(nums.length-1)-i]
  //     if (left in result) {
  //         result[left]++
  //     } else {
  //         result[left] = 1
  //     }
  //
  //     if (right in result) {
  //         result[right]++
  //     } else {
  //         result[right] = 1
  //     }
  //
  //     if (result[left] >= majority) {
  //         return left
  //     } else if (result[right] >= majority) {
  //         return right
  //     }
  // }

  //sorting. With sorted majority element will always be at index n/2
  // nums.sort()
  // return nums[Math.floor(nums.length/2)]

  //boyer-moore voting algorithm
  let canditate = nums[0];
  let count = 0;
  for (const num of nums) {
    if (count === 0) {
      canditate = num;
    }
    count += num === canditate ? 1 : -1;
  }

  return canditate;
};
