'''
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:
    Input: s = "abcabc", k = 3
    Output: ["abc", "bca", "cab"]

Example 2:
    Input: s = "abacab", k = 3
    Output: ["bac", "cab"]

Example 3:
    Input: s = "awaglknagawunagwkwagl", k = 4
    Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
    Explanation:
    Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
    "wagl" is repeated twice, but is included in the output once.

Constraints:
    The input string consists of only lowercase English letters [a-z]
    0 ≤ k ≤ 26
'''
class Solutions():
    def distinctCharSubstr(self, string, k): # Time: O(n*k)
        substrList = []
        for i in range(len(string) - 2): # O(n)
            substr = string[i:i+k]
            # check if substr has k unique chars and not already added
            if (len(set(substr)) == k) and (substr not in substrList): # O(k)
                substrList.append(substr)
        return substrList

    def optimized(self, string, k): # Time: O(n)
        idxDict = dict() # key = char, val = idx of char
        subsets = set()
        start = 0

        for i in range(len(string)):
            if string[i] in idxDict and i-idxDict[string[i]] < k: # Duplicate found, start new substring by moving start
                start = idxDict[string[i]] + 1
            idxDict[string[i]] = i

            if i - start + 1 == k:
                subsets.add(string[start:i + 1])
                start += 1
            #print(idxDict)
        return list(subsets)

    def slidingWindow(self, string, k):
        window = set()
        res = set()

        start = 0
        cur = 0
        while cur < len(string):
            while string[cur] in window:
                window.remove(string[start])
                start += 1
            window.add(string[cur])
            if len(window) == k:
                res.add(string[start:cur+1])
                window.remove(string[start])
                start += 1
            cur += 1
        return list(res)
    
s = Solutions()
l1 = s.distinctCharSubstr("awaglknagawunagwkwagl",4)
l2 = s.optimized("awaglknagawunagwkwagl",4)
l3 = s.slidingWindow("awaglknagawunagwkwagl",4)
print(l1)
print(l2)
print(l3)
