const majorityElement = (nums: number[]) => {
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

  //     if (right in result) {
  //         result[right]++
  //     } else {
  //         result[right] = 1
  //     }

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
// console.log(majorityElement([3,2,3]))
// console.log(majorityElement([2,2,1,1,1,2,2]))

const firstMissingPositive = (nums: number[]) => {
  let current = 1;
  nums.sort((a, b) => a - b);
  console.log(nums);
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
// console.log(firstMissingPositive([1,2,0]))
// console.log(firstMissingPositive([3,4,-1,1]))
// console.log(firstMissingPositive([7,8,9,11,12]))
// console.log(firstMissingPositive([100000, 3, 4000, 2, 15, 1, 99999]))
// console.log(firstMissingPositive([0,2,2,1,1]))

const groupAnagrams = (strs: string[]) => {
  const characterCounts: Record<string, string[]> = {};
  let count = 0;
  const aCode = "a".charCodeAt(0);
  for (const str of strs) {
    const alphabetCount = new Array(26).fill(0);
    for (let i = 0; i < str.length; i++) {
      const index = str[i].charCodeAt(0) - "a".charCodeAt(0);
      alphabetCount[index] += 1;
    }
    const key = alphabetCount.join("");
    if (key in characterCounts) {
      characterCounts[key].push(str);
    } else {
      characterCounts[key] = [str];
    }
  }
  return Object.values(characterCounts);
};
// console.log(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
// console.log(groupAnagrams(["x"]))
// console.log(groupAnagrams([""]))
const frequentK = (nums: number[], k: number) => {
  const frequencies: Record<number, number> = {};
  for (const num of nums) {
    if (num in frequencies) {
      frequencies[num] += 1;
    } else {
      frequencies[num] = 1;
    }
  }

  return Object.entries(frequencies)
    .filter((entry) => entry[1] >= k)
    .map((entry) => entry[0]);
};
// console.log(frequentK([1,2,2,3,3,3], 2))

class EncodeDecode {
  encode(strs: string[]): string {
    const encoded: string[] = [];
    for (const str of strs) {
      encoded.push(`${str.length}#${str}`);
    }
    return encoded.join("");
  }

  decode(str: string): string[] {
    const decoded: string[] = [];
    let index = 0;
    let stringIntArray: string[] = [];
    while (index < str.length) {
      while (str[index] !== "#") {
        stringIntArray.push(str[index]);
        index++;
      }

      const count = parseInt(stringIntArray.join(""));
      index++;
      const stringBuilder: string[] = [];
      for (let c = count; c >= 1; c--) {
        stringBuilder.push(str[index]);
        index++;
      }
      decoded.push(stringBuilder.join(""));
      index++;
    }
    return decoded;
  }
}
// const a = new EncodeDecode()
// let encoded = a.encode(["neet","code","love","you"])
// let decoded = a.decode(encoded)
// console.log(decoded)
// encoded = a.encode(["ne#et","code","love","#you"])
// decoded = a.decode(encoded)
// console.log(decoded)

const longestSequence = (nums: number[]) => {
  const sequenceSet = new Set(nums);
  let longest = 1;

  for (const num of sequenceSet) {
    let currentNum = num - 1;
    if (sequenceSet.has(currentNum)) {
      let count = 2;
      // doing a longest sequence in descending order
      while (sequenceSet.has(--currentNum)) {
        count++;
      }
      longest = Math.max(longest, count);
    }
  }
  return longest;
};

// console.log(longestSequence([2,20,4,10,3,4,5]))
// console.log(longestSequence([0,3,2,5,4,6,1,1]))

const twoSumagain = (nums: number[], target: number) => {
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

console.log(twoSumagain([2, 7, 11, 15], 9)); //[0,1] or [1,0]
