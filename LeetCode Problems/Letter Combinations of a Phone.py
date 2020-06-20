'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


def letterCombinations(digits):
    if digits == "":
        return []
    letters = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
               '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
               '8':['t','u','v'], '9':['w','x','y','z']}
    res = letters[digits[0]][:] # deepcopy first digit (no reference to dict)
    for i in range(1, len(digits)):
        l = len(res)
        digit_i = digits[i]
        res *= len(letters[digit_i]) #[a,b,c]--->[a,b,c,a,b,c,a,b,c]
        for j in range(len(res)):
            if 0 <= j and j < l: # [aa, ba, ca]
                res[j] += letters[digit_i][0]
            elif l <= j and j < 2*l: # [ab, bb, cb]
                res[j] += letters[digit_i][1]
            elif 2*l <= j and j < 3*l: # [ac, bc, cc]
                res[j] += letters[digit_i][2]
            else: # 4 digits
                res[j] += letters[digit_i][3]
    return res
''' 
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        phone = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
                   '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                   '8':['t','u','v'], '9':['w','x','y','z']}
        res = []
        if digits:
            self.backtrack("", digits, res, phone)
        return res
    
    def backtrack(self, subset, digits, res, phone):
        if len(digits) == 0:  # if there is no more digits to check
            res.append(subset)                         
        else: # if there are still digits to check
            for letter in phone[digits[0]]:  # iterate over [a,b,c]
                self.backtrack(subset + letter, digits[1:], res, phone)# append the current letter to the combination
                                                                # and proceed to the next digits
