const isSubsequence = (s: string, t: string) => {
  // let tStart = 0
  // for (let i = 0; i < s.length; i++) {
  //     let found = false
  //     for (; tStart < t.length; tStart++) {
  //         found = s[i] === t[tStart]
  //         if (found) {
  //             break
  //         }
  //     }
  //     if (!found) {
  //         return false
  //     }
  // }
  // return true

  // two pointer approach
  let sPointer = 0;
  let tPointer = 0;
  while (sPointer < s.length && tPointer < t.length) {
    if (s[sPointer] === t[tPointer]) {
      sPointer++;
    }
    tPointer++;
  }
  return sPointer === s.length;
};
// console.log(isSubsequence("abc", "ahbgdc"))
// console.log(isSubsequence("axc", "ahbgdc"))

function reverseWords(s: string): string {
  const answer: string[] = [];
  let end = s.length - 1;
  let start = end - 1;
  while (end >= 0 && start >= 0) {
    if (s[end] === " ") {
      end--;
      start = end - 1;
      continue;
    }
    if (s[start] === " ") {
      answer.push(s.slice(start + 1, end + 1));
      end = start;
    }
    start--;

    if (start === 0 && s[start] !== " ") {
      answer.push(s.slice(start, end + 1).trim());
    }
  }
  return answer.join(" ");
}
// console.log(reverseWords("the sky is blue"));
// console.log(reverseWords("  hello world  "));
// console.log(reverseWords("a good   example"));
// console.log(reverseWords("Je suis tres content"));

// in-progress
function intToRoman(num: number): string {
  const mapconvert: Record<number, string> = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
  };

  const numstr = num.toString();
  let answer: string[] = [];
  for (let i = 0; i < numstr.length; i++) {
    const place = numstr.length - i - 1;
    const digit = parseInt(numstr[i]);
    const total = digit * 10 ** place;
    if ((numstr[i] === "4" || numstr[i] === "9") && total < 1000) {
      const exponent = 1 * 10 ** place;
      answer.push(mapconvert[exponent] + mapconvert[total + exponent]);
    } else if (total >= 500 && total < 1000) {
      answer.push(mapconvert[500]);
      const hundreds = (total - 500) / 100;
      for (let j = 0; j < hundreds; j++) {
        answer.push(mapconvert[100]);
      }
    } else if (total >= 50 && total < 100) {
      answer.push(mapconvert[50]);
      const tens = (total - 50) / 10;
      for (let j = 0; j < tens; j++) {
        answer.push(mapconvert[10]);
      }
    } else if (total >= 5 && total < 10) {
      answer.push(mapconvert[5]);
      const ones = total - 5;
      for (let j = 0; j < ones; j++) {
        answer.push(mapconvert[1]);
      }
    } else {
      const mapvalue = total / digit;
      answer.push(mapconvert[mapvalue].repeat(digit));
    }
  }
  return answer.join("");
}

function toRomanNumeral(num: number): string {
  // Validate input - Roman numerals traditionally represent 1-3999
  if (num < 1 || num > 3999) {
    throw new Error("Number must be between 1 and 3999");
  }

  // Pre-computed lookup table with values in descending order
  // This includes subtractive notation cases (IV, IX, XL, XC, CD, CM)
  // Using arrays instead of objects for better performance
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const numerals = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ];

  // Build result string by greedily selecting largest possible values
  let result = "";

  // Iterate through values from largest to smallest
  for (let i = 0; i < values.length; i++) {
    // Determine how many times current value fits into remaining number
    // Using integer division (Math.floor) to get the count
    const count = Math.floor(num / values[i]);

    // Append the corresponding numeral 'count' times
    // repeat() is O(n) but more efficient than a loop for string concatenation
    if (count > 0) {
      result += numerals[i].repeat(count);
      // Reduce num by the amount we've converted
      num -= values[i] * count;
    }

    // Early exit if we've converted the entire number
    if (num === 0) break;
  }

  return result;
}

console.log(toRomanNumeral(3749)); // "MMMDCCXLIX"
console.log(intToRoman(58)); // "LVIII"
console.log(intToRoman(1994)); // "MCMXCIV"
