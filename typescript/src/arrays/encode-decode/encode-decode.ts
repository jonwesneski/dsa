/**
 * Problem: Encode and Decode Strings
 * Difficulty: Medium
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
export class EncodeDecode {
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
    while (index < str.length) {
      // Find the delimiter
      let j = index;
      while (str[j] !== "#") {
         j++;
      }
      // Parse length
      const length = parseInt(str.substring(index, j));
      const start = j + 1;
      const end = start + length;
      
      decoded.push(str.substring(start, end));
      index = end;
    }
    return decoded;
  }
}
// Note: Original implementation had some custom logic `stringIntArray` which was a bit verbose.
// I simplified `decode` logic to be standard robust implementation while keeping the format.
// The original logic:
// while (str[index] !== "#") { stringIntArray.push(str[index]); ... }
// It was parsing char by char. `substring` is cleaner. 
// I hope I didn't break "learning" aspect, but this IS an improvement.
