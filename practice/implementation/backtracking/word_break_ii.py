"""
Backtracking - Word Break II (hard)

Description:
Given a string s and a dictionary of strings wordDict, add spaces in s to 
construct a sentence where each word is a valid dictionary word. Return all 
such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in 
the segmentation.

Example:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

LeetCode: https://leetcode-cn.com/problems/word-break-ii
"""
from functools import lru_cache 

def word_break_ii(string: str, word_dict: list) -> list:
    """ Backtracking

    We can use DP to check whether the string could be broken, however to get 
    the potential splits, using DP with bottom-up will require a lot of 
    matching, and it will exceed the time limit.

    For example:
    s = "aaaaaaa...aaaaaaaabaaaaaa...aa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa"]

    There is a 'b' in the string and the word list doesn't contain 'b', so we 
    can't break the string, however, DP will still do a lot of searching.

    We can use backtracking with memorization here (top-down).

    For a string s, if its prefix is in the word list, then we can remove it 
    and try with the remaining part. If the whole string could be broken down, 
    then we get a way to split the string.

    Assuming the length of the string is n, then the time complexity of doing
    backtracking is O(N^N). There are a lot duplicated calculations in the 
    process. We can use a hash table to store the indices of the string and 
    the sentence list that start with the index. If we see an visited index, 
    then we can retrieve the result from the hash table.

    We can also use hash set to store the word list, so checking whether a 
    word is in the list will take O(1) rather than O(M), M is the number of 
    words in the word list.

    Time Complexity - O(N*2^N) - Memorization changed the base from N to 2.
    Space Complexity - O(N*2^N) - N is the length of the string, there are 2^N 
    ways to split the string, and for each way, we need to store a string with 
    O(N), so in total O(N*2^N).
    """
    @lru_cache(None)
    def backtracking(index: int) -> list:
        # Recursion termination
        if index == len(string):
            return [[]]
        
        # Result words are in reversed order.
        res = []

        for i in range(index + 1, len(string) + 1):
            # Word with index as beginning and i as end.
            word = string[index:i]

            # Check whether the word is in the word list.
            # If yes, drill down to next level (index = i).
            if word in word_set:
                # Scan from new index i.
                next_word_breaks = backtracking(i)

                # Append the words from backtracking.
                for next_word_break in next_word_breaks:
                    res.append(next_word_break.copy() + [word])
        return res
    
    word_set = set(word_dict)
    break_list = backtracking(0)
    return [" ".join(words[::-1]) for words in break_list]


if __name__ == "__main__":
    string, word_dict = "catsanddog", ["cat","cats","and","sand","dog"]
    print(word_break_ii(string, word_dict))

    string, word_dict = "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    print(word_break_ii(string, word_dict))