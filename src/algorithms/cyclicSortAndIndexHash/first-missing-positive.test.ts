import { firstMissingPositive } from "./first-missing-positive";

test("firstMissingPositive basic", () => {
    expect(firstMissingPositive([1, 2, 0])).toBe(3);
});

test("firstMissingPositive gaps", () => {
    expect(firstMissingPositive([3, 4, -1, 1])).toBe(2);
});

test("firstMissingPositive perfect sequence", () => {
    expect(firstMissingPositive([7, 8, 9, 11, 12])).toBe(1);
});

test("firstMissingPositive with duplicates", () => {
    expect(firstMissingPositive([0, 2, 2, 1, 1])).toBe(3);
});
