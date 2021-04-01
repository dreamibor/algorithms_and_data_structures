"""
Hash Table - Valid Anagram (easy)

Description:
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

LeetCode: https://leetcode-cn.com/problems/valid-anagram/
"""
from collections import defaultdict


def is_anagram_hash_table(source:str, target:str) -> bool:
    """ Using hash table to count the frequency of characters.

    Time Complexity - O(N) - Scanning through the input once.
    Space Complexity - O(1) - the space for hash table will remain the same
    no matter how large N is.
    """
    # Create two hash table for source and target string.
    source_map = defaultdict(int)
    target_map = defaultdict(int)

    # Count the frequency of characters in the string.
    for char in source:
        source_map[char] += 1
    
    for char in target:
        target_map[char] += 1

    # Compare the two hash tables. 
    return source_map == target_map

def is_anagram_hash_array(source:str, target:str) -> bool: 
    """ Using an array to replace hash table.
        
    Time Complexity - O(N) - Scanning through the input once.
    Space Complexity - O(1) - the space for the array (hash table) will remain 
    the same no matter how large N is.
    """
    if len(source) != len(target):
        return False
    
    # Create an array as hash table, assuming the string only 
    # contains 26 lowercase letters.
    table = [0]*26

    for char in source:
        table[ord(char) - ord("a")] += 1
    
    for char in target:
        table[ord(char) - ord("a")] -= 1
        if table[ord(char) - ord("a")] < 0:
            return False
    
    return True

def is_anagram_sort(source:str, target:str) -> bool:
    """ Sort the string and then compare.

    Time Complexity - O(NlogN) - for quick sort.
    Space Complexity - O(1) - Depending on the sorting algorithm, the space 
    complexity could be auxiliary O(1) for heap sort.
    """
    return sorted(source) == sorted(target)

if __name__ == "__main__":
    # Hash table
    s, t = "anagram", "nagaram"
    print(is_anagram_hash_table(s, t))

    s, t = "car", "rat"
    print(is_anagram_hash_table(s, t))

    # Array (hash table)
    s, t = "anagram", "nagaram"
    print(is_anagram_hash_array(s, t))

    s, t = "car", "rat"
    print(is_anagram_hash_array(s, t))

    # Sort and compare
    s, t = "anagram", "nagaram"
    print(is_anagram_sort(s, t))

    s, t = "car", "rat"
    print(is_anagram_sort(s, t))