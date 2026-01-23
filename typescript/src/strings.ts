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
console.log(reverseWords("Je suis tres content"));

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
    const place = numstr.length - i;
    const digit = parseInt(numstr[i]);
    const total = digit * 10 ** (place - 1);
    if ((numstr[i] === "4" || numstr[i] === "9") && total < 1000) {
      answer.push(mapconvert[1] + mapconvert[digit + 1]);
    } else {
      const mapvalue = total / digit;
      answer.push(mapconvert[mapvalue].repeat(place));
    }
  }
  return answer.join("");
}

// console.log(intToRoman(3749)); // "MMMDCCXLIX"
// console.log(intToRoman(58)); // "LVIII"
// console.log(intToRoman(1994)); // "MCMXCIV"
