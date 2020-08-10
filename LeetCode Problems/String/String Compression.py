'''
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
    Could you solve it using only O(1) extra space?
 
Example 1:
    Input:
    ["a","a","b","b","c","c","c"]

    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:
    Input:
    ["a"]

    Output:
    Return 1, and the first 1 characters of the input array should be: ["a"]

    Explanation:
    Nothing is replaced.

Example 3:
    Input:
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    Output:
    Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

    Explanation:
    Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
    Notice each digit has it's own entry in the array.


Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''

class Solution:
    def compress(self, chars): # Time Complexity: O(n), Space Complexity: 0(1)
        idx = 1 # the index where the next modification will be
        cur = chars[0] # the current character
        freq = 1 # the frequency of current character
        
        # For same chars, increment freq, if new char found, modify element
        for i in range(1, len(chars)):
            if chars[i] != cur: # new char
                # append freq of the old char
                if freq == 1:
                    chars[idx] = chars[i]
                    idx += 1
                elif 10 >freq > 1:
                    chars[idx] = str(freq)
                    chars[idx+1] = chars[i]
                    freq = 1
                    idx += 2
                elif freq >= 10:
                    chars[idx] = str(freq)[0]
                    chars[idx+1] = str(freq)[1]
                    chars[idx+2] = chars[i] 
                    freq = 1
                    idx += 3
                cur = chars[i]
            else:
                freq += 1
        
        # The frequency of last char is not added by loop
        if 10 >freq > 1:
            chars[idx] = str(freq)
            idx +=1
        elif freq >= 10:
            chars[idx] = str(freq)[0]
            chars[idx+1] = str(freq)[1]
            idx +=2
            
        return idx
