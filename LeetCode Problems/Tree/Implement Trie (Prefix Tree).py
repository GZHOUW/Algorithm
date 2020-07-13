'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        s = self.root
        for char in word:
            if char not in s:  # new branch
                s[char] = dict()
                s = s[char]
            else: # the letter exists in this layer, go to next layer and check next char
                s = s[char]
        
        # After loop ends, a word has been inserted, mark the end of this word
        s["isWordEnd"] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        s = self.root
        for char in word:
            if char not in s:
                return False
            else:
                s = s[char]
        if "isWordEnd" in s:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        s = self.root
        for char in prefix:
            if char not in s:
                return False
            else:
                s = s[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
