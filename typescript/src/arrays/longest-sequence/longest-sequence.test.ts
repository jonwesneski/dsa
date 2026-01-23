import { longestSequence } from "./longest-sequence";

test("longestSequence basic", () => {
    expect(longestSequence([100, 4, 200, 1, 3, 2])).toBe(4); // 1,2,3,4
});

test("longestSequence mixed", () => {
    expect(longestSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])).toBe(9); // 0,1,2,3,4,5,6,7,8
});

test("longestSequence empty", () => {
    expect(longestSequence([])).toBe(0);
});
