'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
'''
def checkValidString(s):
    # stack 1, let * be (
    stack = []        
    # go through s from left to right
    for char in s:
        if char =='(' or char =='*':
            stack.append(char)
        else: # char == ')'
            if len(stack) == 0: # right before left ')*' or too many right '(**)))))'
                return False
            else:
                stack.pop()

    # stack 2, let * be )
    stack = []        
    # go through s from right to left
    for char in s[::-1]:
        if char == ')' or char == '*':
            stack.append(char)
        else:
            if len(stack) == 0: # left after right '*(' or too many left '((((*)*'
                return False
            else:
                stack.pop()

    # if passed both tests, return true
    return True
