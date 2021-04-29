"""
Trie - Short Encoding of Words (medium)

A valid encoding of an array of `words` is any reference string `s` and array 
of `indices` indices such that:
* `words.length == indices.length`
* The reference string `s` ends with the '#' character.
* For each index `indices[i]`, the substring of `s` starting from `indices[i]` 
and up to (but not including) the next '#' character is equal to `words[i]`.

Given an array of `words`, return the length of the shortest reference string 
`s` possible of any valid encoding of `words`.

Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: 
A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the 
next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next 
'#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the 
next '#' is underlined in "time#bell#"

LeetCode: https://leetcode-cn.com/problems/short-encoding-of-words/
"""

def minimum_length_encoding_postfix(words: list) -> int:
    """ Store Postfixes
    
    If word X is the postfix of word Y, then there is no need to store word 
    X. For example, "me" is the postfix of "time", so we can ignore "me". If 
    Y doesn't exist in any word X's postfix, then we shall include Y in the 
    encoding.

    Time Complexity - O(Σ(w_i)^2) - Where w_i is the length of word words[i].
    For each word, it has w_i postfixes, for each postfix, we need O(w_i) to 
    calculate the hash value to look up in the set.
    Space Complexity - O(Σw_i) - For storing all words in the set.
    """
    postfixes = set(words)

    for word in words:
        for i in range(1, len(word)):
            # Check if the postfix is in the set.
            if word[i:] in postfixes:
                # Remove the postfix if it exists in the set.
                postfixes.remove(word[i:])
    
    # return len(postfixes) + len("".join(postfixes))
    return sum(len(word) + 1 for word in postfixes)

def minimum_length_encoding_trie(words: list) -> int:
    """ Trie

    The target is to store all words which are not postfixes of other words. 
    We can reverse the word, and store them in a trie. For example, for words 
    "time" and "me", we can reverse them to "emit" and "em", then we can 
    insert them into a trie.

    After we've insert all words, we only need to count the leaf nodes in the 
    trie, and plus one for the hashtag.

    Time Complexity - O(Σw_i) - Where w_i is the length of word words[i]. For 
    each character in each word, we only need constant operations.
    Space Complexity - O(S*Σw_i) - For the trie, where S is the alphabet or 
    character set size.
    """
    # Remove duplicate words.
    words = list(set(words))

    # Build a trie for given words.
    trie = {}
    # Store the last node for each word.
    # For example, store the value corresponding to "t" for "emit".
    nodes = []

    for word in words:
        node = trie
        # Reverse characters in the word, and insert each char into trie.
        for char in word[::-1]:
            # Retrieve the next node, if not found, create a empty node.
            node = node.setdefault(char, {})

        nodes.append(node)
    
    # res = 0
    # for w,c in zip(words,nodes):
    #     if len(c) == 0:
    #         res += len(w) + 1
    
    # return res
    return sum(len(w) + 1 if len(c) == 0 else 0 for w, c in zip(words, nodes))


if __name__ == "__main__":
    words = ["time", "me", "bell"]
    print(minimum_length_encoding_postfix(words))
    print(minimum_length_encoding_trie(words))