import { majorityElement } from "./majority-element";

test("majorityElement basic", () => {
  expect(majorityElement([3, 2, 3])).toBe(3);
});

test("majorityElement extended", () => {
  expect(majorityElement([2, 2, 1, 1, 1, 2, 2])).toBe(2);
});
