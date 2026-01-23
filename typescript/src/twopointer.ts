//Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.
const threeSum = (nums: number[]) => {
  const result: [number, number, number][] = [];

  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] == nums[i - 1]) {
      continue;
    }

    let leftPointer = i + 1;
    let rightPointer = nums.length - 1;
    while (leftPointer < rightPointer) {
      const total = nums[i] + nums[leftPointer] + nums[rightPointer];
      if (total === 0) {
        result.push([nums[i], nums[leftPointer], nums[rightPointer]]);
        leftPointer++;
      } else if (total > 0) {
        rightPointer--;
      } else {
        leftPointer++;
      }
    }
  }

  return result;
};
// console.log(threeSum([-1,0,1,2,-1,-4]))
// console.log(threeSum([0,1,1]))
// console.log(threeSum([0,0,0]))
// console.log(threeSum([-2,-2,0,0,2,2]))

const twoSum = (numbers: number[], target: number): number[] => {
  let leftPointer = 0;
  let rightPointer = numbers.length - 1;
  while (leftPointer < rightPointer) {
    const total = numbers[leftPointer] + numbers[rightPointer];
    if (total === target) {
      return [leftPointer + 1, rightPointer + 1];
    } else if (total < target) {
      leftPointer++;
    } else {
      rightPointer--;
    }
  }

  return [];
};
// console.log(twoSum([2,7,11,15], 9))

const maxArea = (height: number[]): number => {
  let leftPointer = 0;
  let rightPointer = height.length - 1;
  let answer = 0;

  while (leftPointer < rightPointer) {
    let currentArea =
      Math.min(height[leftPointer], height[rightPointer]) *
      (rightPointer - leftPointer);
    if (height[leftPointer] < height[rightPointer]) {
      leftPointer++;
    } else {
      rightPointer--;
    }
    console.log(currentArea, leftPointer, rightPointer);
    answer = Math.max(answer, currentArea);
  }

  return answer;
};
//console.log(maxArea([1,8,6,2,5,4,8,3,7]))
//console.log(maxArea([1,2]))

const maxAreaAgain = (height: number[]): number => {
  let l = 0;
  let r = height.length - 1;
  let maxArea = 0;
  while (l < r) {
    const area = Math.min(height[l], height[r]) * (r - l);
    maxArea = Math.max(maxArea, area);
    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
  }
  return maxArea;
};
