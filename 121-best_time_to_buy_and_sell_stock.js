// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

/**
 * @param {number[]} prices
 * @return {number}
 */
function maxProfit(prices) {
    let result = Number.NEGATIVE_INFINITY
    let len = prices.length
    if (len === 1) return 0 // 0 profit

    //min value threshold in current element
    let mins = new Array(len).fill(Number.NEGATIVE_INFINITY)
    mins[0] = prices[0]

    let dp = new Array(len).fill(0)
    dp[0] = 0

    for (let i = 0; i < len; i++) {
        if (prices[i + 1] - mins[i] > 0) {
            dp[i + 1] = prices[i + 1] - mins[i]
            mins[i + 1] = mins[i]
        } else {
            dp[i + 1] = 0
            mins[i + 1] = prices[i + 1]
        }
        if (result < dp[i + 1]) result = dp[i + 1]
    }
    return result
}

// let prices = [7,1,5,3,6,4]
// //let prices = [1, 2]
// console.log(maxProfit(prices))