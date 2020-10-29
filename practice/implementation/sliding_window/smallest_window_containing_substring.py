"""
Sliding window - Smallest Window containing Substring (hard)

Description:
Given a string and a pattern, find the smallest substring in the given string 
which has all the characters of the given pattern.

Example:
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Notes: 
1. Characters in pattern could repeat. i.e. "aacc".
2. Be clear that there is only one substring meet the requirement.

Time Complexity - O(N+M) - N is the number of characters in the input string.
Space Complexity - O(M) - M is the number of distinct characters in the pattern.

LeetCode link: https://leetcode-cn.com/problems/minimum-window-substring/
"""


def find_substring(string, pattern):
    # Keep a running count of every matching instance of a character.
    window_start, matched_char_num, substring_start = 0, 0, 0 
    char_map = {}
    min_len = len(string) + 1

    for char in pattern:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    
    # Try to extend the range [window_start, window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_map:
            char_map[right_char] -= 1
            # Count every matching of a character
            if char_map[right_char] >= 0: 
                matched_char_num += 1
        
        # Whenever we have matched all the characters, we will try to shrink the 
        # window from the beginning, finish as soon as we remove a matched character.
        while matched_char_num == len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                substring_start = window_start
        
            left_char = string[window_start]
            window_start += 1

            if left_char in char_map:
                # Note that we could have redundant matching characters, therefore 
                # we'll decrement the matched count only when a useful occurrence of 
                # a matched character is going out of the window
                if char_map[left_char] == 0:
                    matched_char_num -= 1
                char_map[left_char] += 1
    
    if min_len > len(string):
        return ""
    return string[substring_start: substring_start + min_len]


if __name__ == "__main__":
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))