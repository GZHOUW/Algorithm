'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

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
    
''' better solution
def letterCombinations(digits): 
    phone = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
               '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
               '8':['t','u','v'], '9':['w','x','y','z']}


    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output
'''
