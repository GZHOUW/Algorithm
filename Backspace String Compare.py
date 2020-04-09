'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

'''

def backspaceCompare(S, T):
    S_stack = []
    T_stack = []
    for char in S:
        if char != '#':
            S_stack.append(char)
        elif S_stack: # char is # and stack is not empty
            S_stack.pop()

    for char in T:
        if char != '#':
            T_stack.append(char)
        elif T_stack: # char is # and stack is not empty
            T_stack.pop()

    return S_stack == T_stack
 
