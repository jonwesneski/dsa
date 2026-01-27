const findRepeatedDnaSequences = (s: string): string[] => {
  const seen = new Set<string>();
  const repeated = new Set<string>();
  const length = 10;
  for (let r = length; r < s.length; r++) {
    const temp = s.slice(r - length, r);
    if (seen.has(temp)) {
      repeated.add(temp);
    }
    seen.add(temp);
  }
  return [...repeated];
};

// console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")); // ["AAAAACCCCC","CCCCCAAAAA"]
// console.log(findRepeatedDnaSequences("AAAAAAAAAAAAA")); // ["AAAAAAAAAA"]
// console.log(findRepeatedDnaSequences("AAAAAAAAAAA")); // ["AAAAAAAAAA"]
