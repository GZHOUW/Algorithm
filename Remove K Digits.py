'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
'''

def removeKdigits(num, k):
    stack = []

    for i in range(len(num)):
        '''
        k > 0: still need to delete more elements
        stack: stack is not empty, if empty 
        '''
        while k > 0 and stack and num[i] < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num[i])

    # Edge case: '111112', k=3 --> '11111',k=2
    while k != 0:
        stack.pop()
        k -= 1

    # delete leading zeros
    while stack:
        if stack[0] == '0':
            stack = stack[1:]
        else:
            break

    if not stack:
        return "0"
    return ''.join(stack)

