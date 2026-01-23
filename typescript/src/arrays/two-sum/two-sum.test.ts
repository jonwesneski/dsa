import { twoSum } from "./two-sum";

test("twoSum basic", () => {
    const result = twoSum([2, 7, 11, 15], 9);
    // [0, 1] or [1, 0]
    expect(result.sort()).toEqual([0, 1]);
});

test("twoSum none", () => {
    expect(twoSum([1, 2], 10)).toEqual([-1, -1]);
});
