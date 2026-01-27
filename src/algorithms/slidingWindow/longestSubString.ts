const longestSubStringLength = (s: string): number => {
  const cache = new Set<string>();
  let windowStart = 0;
  let maxLength = s.length ? -Infinity : 0;
  for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
    while (cache.has(s[windowEnd])) {
      // Remove value of start/left from cache and make window smaller
      cache.delete(s[windowStart]);
      windowStart += 1;
    }
    // The char is unique, determine if substring is longest
    cache.add(s[windowEnd]);
    maxLength = Math.max(maxLength, cache.size);
  }
  return maxLength;
};
// console.log(longestSubStringLength("abcabcbb")); // 3 "abc","bca", or "cab"
// console.log(longestSubStringLength("bbbbb")); // 1
// console.log(longestSubStringLength("pwwkew")); // 3 "wke"; not "pwke", it is a subsequence and not a substring.
// console.log(longestSubStringLength("aab")); // 2
console.log(longestSubStringLength("qrsvbspk")); // 5
// console.log(longestSubStringLength("")); // 0
