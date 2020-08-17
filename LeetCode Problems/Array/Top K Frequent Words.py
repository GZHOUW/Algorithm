import collections
import heapq

class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        # the first element of heap is always the smallest (according to the customized < in class Word)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k: # keep popping until k (largest) elements left
                heapq.heappop(heap)
        res = []
        for _ in range(k): # append remainng elements to res
            res.append(heapq.heappop(heap).word)
        return res[::-1]
  
   def topKFrequentSort(self, words, k): # sort method, time=O(nlogn), space = O(n)
        '''
        Algorithm: 1. Create a dictionary {word: frequency}
                   2. Sort the keys by negative frequency (descending) and alphabet if same freq
        '''
        res = []
        freq = {} # O(n) space
        for word in words: # O(n) time
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        
        words = freq.keys()
        
        # lambda fcn: returns whats after ':'; sort key: sorts the list by comparing the key
        #  -freq[word] --> sort words by reversed frequency order (descending)
        #  word --> if -freq[word] are equal, sort by alphabetical order
        words = sorted(words, key = lambda word: (-freq[word], word))
        return words[:k]
        

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    # overload < and == for the operation of heap
    def __lt__(self, other):  # overload '<' operator
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):  # overload '==' operator
        return self.freq == other.freq and self.word == other.word

s = Solution()
res = s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print(res)
