// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
// the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

/**
 * @param {number[]} nums
 * @return {number}
 */
function rob(nums) {
    let len = nums.length
    if (len === 1) {
        return nums[0]
    }
    if (len === 2) {
        return nums[0] > nums[1] ? nums[0] : nums[1]
    }
    let result = Number.MIN_VALUE
    let dp = new Array(len).fill(0)
    dp[0] = nums[0]
    if (result < dp[0]) result = dp[0]
    dp[1] = nums[0] > nums[1] ? nums[0] : nums[1]
    if (result < dp[1]) result = dp[1]

    for (let index = 2; index < len; index++) {
        dp[index] = findMax(dp, index - 1) + nums[index]
        if (dp[index] > result) {
            result = dp[index]
        }
    }

    return result
};

/**
 * @description: 找到最大值
 */
function findMax(arr, lastIndex) {
    let result = Number.NEGATIVE_INFINITY
    for (let index = 0; index < lastIndex; index++) {
        let item = arr[index]
        if (item > result) {
            result = item
        }
    }
    console.log(`max => ${result}`)
    return result
}

// let nums = [2, 1, 1, 2];
let nums = [1,3,1,3,100]
console.log(rob(nums))