'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''

class Solution:
    def minRemoveToMakeValid(self,s):
        '''
        Algorithm: 1. use stack to remove all invalid ')', either extra or no corresponding '('
                   2. keep removeing remaining '(' from the right until there are same num of ( and )
        '''
        stack = []
        new_s = ""
        for cur in range(len(s)):
            if s[cur] == '(':
                stack.append(')')
                new_s += s[cur]
            elif s[cur] == ')':
                if stack:
                    new_s += stack.pop()
            else:
                new_s += s[cur]
                
        # there might be extra "(" remaining
        new_s2 = ""
        extraL = len(stack)
        for i in range(len(new_s)-1,-1,-1):
            
            if new_s[i] == '(' and extraL > 0:
                extraL -= 1
            else:
                new_s2 += new_s[i]
        return new_s2[::-1]
                        
