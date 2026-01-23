const bucketSort = (nums: number[]): number[] => {
  const largest = Math.max(...nums);
  const magicNumber = largest / nums.length;
  const buckets = Array.from<number, number[]>(
    { length: nums.length },
    () => []
  );
  for (const num of nums) {
    let index = Math.floor(num / magicNumber);
    if (index >= nums.length) {
      index = nums.length - 1;
    }
    buckets[index].push(num);
  }

  // Now we just do a regular sort on the buckets arrays and flatten
  for (const bucket of buckets) {
    console.log(bucket);
  }
  return buckets.flat();
};
console.log(bucketSort([12, 4, 11, 90, 99, 3, 40, 41]));
