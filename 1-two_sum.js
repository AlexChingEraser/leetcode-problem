// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    let res = []
    //key: 减值, value: 减值对应前的index
    let cache = {}
    const len = nums.length

    for (let i = 0; i < len; ++i) {
        let curValue = nums[i]
        let substractValue = target - curValue

        //if (curValue > target) continue 负数情况下该判断语句失效
        if (typeof cache[curValue] !== 'undefined') {
            res = [i, cache[curValue]]
            break
        }
        cache[substractValue] = i
    }

    return res
};

// let nums = [-3,4,3,90]
// let target = 0
// console.log(twoSum(nums, target))