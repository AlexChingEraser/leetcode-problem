// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
// A subarray is a contiguous part of an array.

/**
 * @param {number[]} nums
 * @return {number | null} 如果为null则说明计算失败
 */
function maxSubArray(nums) {
    let len = nums.length
    let dp = new Array(len).fill(0)
    dp[0] = nums[0]
    let result = dp[0]

    //dp[i]: at the last index of nums[i], the max subarray
    //index should be start at 0, consider the siuation: [-1]
    //cache `max` value, speed up exec time
    for (let index = 0; index < len - 1; index++) {
        if (nums[index + 1] + dp[index] > nums[index + 1]) {
            dp[index + 1] = nums[index + 1] + dp[index]
        } else {
            dp[index + 1] = nums[index + 1]
        }
        if (dp[index + 1] > result) {
            result = dp[index + 1]
        }
    }

    // in js, the very little value => use `Number.NEGATIVE_INFINITY`, not `Number.MIN_VALUE`
    // return dp.reduce((max, item) => {
    //     max = max < item ? item : max
    //     return max
    // }, Number.NEGATIVE_INFINITY)
    return result
};

//let nums = [-2,1,-3,4,-1,2,1,-5,4]
//let nums = [-1]
//console.log(maxSubArray(nums))
