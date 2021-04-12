"""
Trie - Implement Trie (medium)

Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings. There are various 
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
* Trie() Initializes the trie object.
* void insert(String word) Inserts the string word into the trie.
* boolean search(String word) Returns true if the string word is in the trie 
(i.e., was inserted before), and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously 
inserted string word that has the prefix prefix, and false otherwise.

Example:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
word and prefix consist only of lowercase English letters.

LeetCode: https://leetcode-cn.com/problems/implement-trie-prefix-tree
"""

class Trie:
    """
    Time Complexity:
    1. For initialization - O(1)
    2. For other operations - O(|S|) where |S| is the length of the inserted 
    or searched string.

    Space Complexity - O(|T|*Σ) - where |T| is the total length of inserted 
    string, Σ is the size of character size, here Σ = 26.
    """
    def __init__(self):
        """ Initialize your data structure here. """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        node = self.root

        for char in word:
            # The setdefault() method returns the value of the item with the 
            # specified key.If the key does not exist, insert the key, with 
            # the specified value.
            node = node.setdefault(char, {})
        
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        node = self.root

        for char in word:
            if char not in node:
                return False
            
            node = node[char]
        
        return self.end_of_word in node 

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the 
        given prefix.
        """
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))