"""
Sliding window - Permutation in a String (hard)

Description:
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Example: 
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Time Complexity - O(N+M) or O(N)- N is the number of characters in the input string.
Space Complexity - O(M) or O(1)- M is the number of distinct characters in the pattern.

LeetCode link: https://leetcode-cn.com/problems/permutation-in-string/
"""
from collections import defaultdict


def find_permutation(string: str, pattern:str) -> bool:
    window_start = 0
    num_matched = 0
    char_map = defaultdict(int)

    # Scan the pattern and get the character to frequency map first.
    for char in pattern:
        char_map[char] += 1

    # Scan through the input string and find pattern permutation if possible.
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_map:
            char_map[right_char] -= 1
            if char_map[right_char] == 0:
                num_matched += 1

        print(f"Current window string: {string[window_start: window_end+1]}") 
        print(f"Current character map: {char_map}")

        if num_matched == len(char_map):
            return True
        
        if (window_end - window_start + 1) >= len(pattern):
            left_char = string[window_start]
            if left_char in char_map:
                if char_map[left_char] == 0:
                    num_matched -= 1
                char_map[left_char] += 1
            window_start += 1

    return False

if __name__ == "__main__":
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))
    print('Permutation exist: ' + str(find_permutation("ccccbbbbaaaa", "abc")))
    print('Permutation exist: ' + str(find_permutation("eidboaoo", "ab")))
    print('Permutation exist: ' + str(find_permutation("ab", "eidboaoo"))) # Edge case: pattern is longer than string.
