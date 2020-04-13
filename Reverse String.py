'''
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

class Solution:
    def reverseString(self, s):
        self.swap(s, 0, len(s) - 1) # start with left = first, right = last
    
    def swap(self, s, left, right):
        if left >= right: # base case
            print('do nothing')
        else:# left < right:
            s[left], s[right] = s[right], s[left]
            self.swap(s, left + 1, right - 1)
