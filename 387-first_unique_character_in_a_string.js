/**
 * Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
 * [model]: first unique character
 * [interface]: firstUniqueChar
 * [implement]: hashmap [char]count, char is 26 lower case characters
 */

const TOTAL_CHARS = 26
const BASE_CHAR = 'a'

/**
 * count first no-reapted char in given string
 * @param {String} str 
 * @return {String} ret
 */
function firstUniqueChar(str) {
    /**
     * minus two characters, because in js like 'z' - 'a' == 'NaN'
     * @param {String} c1 
     * @param {String} c2 
     */
    function minusChar(c1, c2) {
        return c1.charCodeAt(0) - c2.charCodeAt(0)
    }
    
    //other way: const charArray = new Array(26).fill(0)
    let map = new Object()
    for (let i = 0; i < TOTAL_CHARS; ++i) {
        map[i] = 0 //init map with [index] -> 0, means a -> 0
    }

    for (let i = 0; i < str.length; ++i) {
        map[minusChar(str[i], BASE_CHAR)] += 1
    }

    for (let i = 0; i < str.length; ++i) {
        if (map[minusChar(str[i], BASE_CHAR)] == 1) {
            return i
            break
        }
    }
    return -1
}