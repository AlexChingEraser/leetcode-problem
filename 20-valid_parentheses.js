// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:
// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

/**
 * @param {string} s
 * @return {boolean} 是否是有效的括号
 */
function isValid(s) {
    const map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    let stack = []
    const pushElements = ['(', '[', '{']
    for (let index = 0; index < s.length; index++) {
        const element = s[index];
        // is positive parenthese
        if (pushElements.includes(element)) {
            stack.push(map[s[index]])
        } else {
            if (stack.pop() !== s[index]) return false
        }
    }
    if (stack.length) return false
    return true
};

//let s = "()[]{}"
//console.log(isValid(s))