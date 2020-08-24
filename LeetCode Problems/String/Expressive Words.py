'''
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
Given a list of query words, return the number of words that are stretchy. 

Example:
    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
'''

class Solution:
    def expressiveWords(self, S, words):
        if not S:
            return 0
        numMatch = 0
        for word in words:
            if self.isMatch(S, word):
                numMatch += 1
        return numMatch
    
    def isMatch(self, s, w):
        i = j = 0
        while i < len(s):
            if  s[i] != w[j]:
                return False
            else:
                cur = s[i]
            s_num = w_num = 0
            
            # get the number of current char in both s and w
            while i < len(s) and s[i] == cur:
                i += 1
                s_num += 1
                
            while j < len(w) and w[j] == cur:
                j += 1
                w_num += 1
            
            # if equal num of chars, pass; if w have more chars or is s has <3 chars, false
            if s_num < w_num:
                return False
            elif s_num > w_num and s_num < 3:
                return False
            
            # if one ended and the other still has more elements
            if (i<len(s) and j>=len(w)) or (i>=len(s) and j<len(w)):
                return False
        return True
        
