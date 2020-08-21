'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
  Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
  Output: true
  Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
  Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
  Output: false
  Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
  
Example 3:
  Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
  Output: false
  Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

class Solution:
    '''
    Algorithm: compare each element with the next element, if smaller (self defined) in lexi order (b<a), return False
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        
        for idx in range(len(order)):
            orderDict[order[idx]] = idx
        self.orderDict = orderDict
        
        for i in range(len(words)-1):
            if self.lessThan(words[i], words[i+1]):
                print(self.lessThan(words[i-1], words[i]))
                return False
        return True
    
    def lessThan(self, cur, other):
        for i in range(min(len(cur), len(other))):
            if self.orderDict[cur[i]] > self.orderDict[other[i]]: # greater idx means smaller
                return True
            elif self.orderDict[cur[i]] < self.orderDict[other[i]]:
                return False
            else: #equal
                continue
        
        if len(cur) > len(other):
            return True
        else:
            return False
