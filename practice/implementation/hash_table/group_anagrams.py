"""
Hash Table - Group Anagrams

Description:
Given an array of strings strs, group the anagrams together. You can return the answer 
in any order. An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],
        ["nat","tan"],
        ["ate","eat","tea"]]

LeetCode: https://leetcode-cn.com/problems/group-anagrams/
"""
from collections import defaultdict


def group_anagrams_array(strings: str) -> list:
    """ Count the character frequency in an array and use it as the hash table key.

    Time Complexity - O(N*(K + |Σ|)) - N is the number of strings in the input, K is the 
    maximum length of strings, while |Σ| is the number of characters, here we only have 
    26 lowercase letters. We are going to iterate through N strings, For each string, we 
    will use O(K) time to calculate the frequency of each character, and then we need O(|Σ|) 
    to convert the array into hash table key and update the hash table with O(1).
    Space Complexity - O(N * (K + |Σ|)) - Using hash table to save all the strings.
    """
    anagram_map = defaultdict(list)

    for string in strings:
        # Use the character as index of the array.
        counts = [0] * 26
        # Count the frequency of each character.
        for char in string:
            counts[ord(char) - ord("a")] += 1
        
        # Convert the list to tuple, so it can be a key of hash table.
        anagram_map[tuple(counts)].append(string)
    
    # Return all the values in the hash table as list.
    return list(anagram_map.values())


def group_anagrams_sort(strings: str) -> list:
    """ Sort the string as the hash table key.

    Time Complexity - O(N*K*logK) - N is the number of strings, K is the maximum length of 
    the string. We iterate each string once and need O(K*logK) to sort the string.
    Space Complexity - O(NK) - For the hash table.
    """
    anagram_map = defaultdict(list)

    for string in strings:
        # sorted(string) will return a list of characters. so we need 
        # to join them together as a string to be the key for the hash 
        # table. 
        key = "".join(sorted(string))
        anagram_map[key].append(string)
    
    # Return all the values in the hash table as list.
    return list(anagram_map.values())



if __name__ == "__main__":
    # Hash table
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams_array(strs))

    strs = [""]
    print(group_anagrams_array(strs))

    strs = ["a"]
    print(group_anagrams_array(strs))

    # Sort
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams_sort(strs))

    strs = [""]
    print(group_anagrams_sort(strs))

    strs = ["a"]
    print(group_anagrams_sort(strs))