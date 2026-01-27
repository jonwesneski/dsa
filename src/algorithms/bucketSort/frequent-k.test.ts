import { topKFrequent } from "./frequent-k";

test("frequentK basic", () => {
  // [1,1,1,2,2,3], k=2 -> [1,2] (assuming standard problem)
  // Code logic: filter entry[1] >= k.
  // [1,2,2,3,3,3], k=2 -> 2 is freq 2, 3 is freq 3. 1 is freq 1.
  // Returns [2, 3] (order not guaranteed by Object keys usually, but small ints often sorted)

  const result = topKFrequent([1, 2, 2, 3, 3, 3], 2);
  expect(result.sort()).toEqual([2, 3]);
});
