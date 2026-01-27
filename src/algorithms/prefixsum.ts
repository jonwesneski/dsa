const rangeIncrement = (n: number, a: Array<[number, number, number]>): number => {
    let result = 0

    const myArray = new Array(n).fill(0)
    for (let i = 0; i < a.length; i++) {
        for (let j=a[i][0]; j <= a[i][1];j++) {
            myArray[j] += a[i][2]
            result = Math.max(result, myArray[j])
        }
    }
    console.log(myArray)
    return result
}
// console.log(rangeIncrement(5, [[0, 1, 100], [1, 4, 100], [2, 3, 100]]))
// console.log(rangeIncrement(4, [[1, 2, 603], [0, 0, 286], [3, 3, 882]]))
const equilibrium = (arr: Array<number>) => {
    const prefixSums = new Array(arr.length).fill(0)
    const suffixSums = new Array(arr.length).fill(0)

    prefixSums[0] = arr[0]
    suffixSums[arr.length-1] = arr[arr.length-1]

    for (let i = 1; i < arr.length; i++) {
        prefixSums[i] = prefixSums[i-1] + arr[i]
    }

    for (let i = arr.length-2; i >= 0; i--) {
        suffixSums[i] = suffixSums[i+1] + arr[i]
    }

    for (let i = 0; i < arr.length; i++) {
        if (prefixSums[i] === suffixSums[i]) {
            return i
        }
    }

    return -1
}
// console.log(equilibrium([1, 2, 0, 3]))
// console.log(equilibrium([1, 1, 1, 1]))
// console.log(equilibrium([1, 1, 1, 1, 1]))
// console.log(equilibrium([-7, 1, 5, 2, -4, 3, 0]))

const leftRight = (arr: Array<number>) => {
    let leftSum = 0
    for (let i = 0; i < arr.length; i++) {
        leftSum += arr[i]
    }

    let rightSum = 0
    for (let i = arr.length-1; i >= 0; i--) {
        rightSum += arr[i]
        leftSum -= arr[i]
        if (rightSum === leftSum) {
            return [arr.slice(0,i), arr.slice(i)]
        }
    }

    return 'Not Possible'
}
// console.log(leftRight([1,2,3,4,5,5]))
// console.log(leftRight([4,1,2,3]))
// console.log(leftRight([4,3,2,1]))

const meanRange = (arr: Array<number>, queries: [number, number][]) => {
    const prefixSums = new Array(arr.length+1).fill(0)
    prefixSums[1] = arr[0]
    for (let i = 1; i < arr.length; i++) {
        prefixSums[i+1] = prefixSums[i] + arr[i]
    }

    const results: number[] = []
    for (const query of queries) {
        const rangeCount = query[1] - (query[0] - 1)
        const rangeSum = prefixSums[query[1]] - prefixSums[query[0]-1]
        results.push(Math.floor(rangeSum/rangeCount))
    }
    return results
}
// console.log(meanRange([3, 7, 2, 8, 5], [[1, 3], [2, 5]]))
// console.log(meanRange([10, 20, 30, 40, 50, 60], [[4, 6]]))

const productExceptSelf = (nums: number[]) => {
    const results = new Array<number>(nums.length)
    results[0] = 1
    for (let i = 1; i < nums.length; i++) {
        results[i] = results[i-1] * nums[i-1]
    }

    let right = 1
    for (let i = nums.length-1; i >= 0; i--) {
        results[i] *= right
        right *= nums[i]
    }

    return results
}
// console.log(productExceptSelf([1,2,3,4]))