//Use this pattern when dealing with problems involving contiguous subarrays or substrings.
const findMaxAverage = (nums: number[], k: number): number => {
    if (nums.length === 1) {
        return nums[0] / k
    }

    let something: number | undefined = undefined
    //nums.sort((a, b) => a - b)

    let leftPointer = 0
    let rightPointer = leftPointer + (k-1)
    while (rightPointer < nums.length) {
        let sum = 0
        for (let i = leftPointer; i <= rightPointer; i++) {
            sum += nums[i]
        }

        if (something === undefined) {
            something = sum
        } else {
            something = Math.max(something, sum)
        }
        leftPointer++
        rightPointer++
    }



    return something! / k
}
console.log(findMaxAverage([1,12,-5,-6,50,3], 4))
console.log(findMaxAverage([5], 1))
console.log(findMaxAverage([0,1,1,3,3], 4))