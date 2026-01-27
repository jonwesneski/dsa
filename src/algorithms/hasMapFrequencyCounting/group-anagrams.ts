/**
 * Problem: Group Anagrams
 * Difficulty: Medium
 * Time Complexity: O(N * K)
 * Space Complexity: O(N * K)
 */
export const groupAnagrams = (strs: string[]) => {
  const characterCounts: Record<string, string[]> = {};
  
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
