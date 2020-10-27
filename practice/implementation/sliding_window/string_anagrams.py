"""
Sliding window - String Anagrams (hard)

Description:
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following 
six anagrams: abc, acb, bac, bca, cab, cba.

Write a function to return a list of starting indices of the anagrams of the pattern 
in the given string.

Example: 
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

Time Complexity - O(N+M) or O(N)- N is the number of characters in the input string.
Space Complexity - O(M) or O(1)- M is the number of distinct characters in the pattern.

LeetCode link: https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
"""

def find_string_anagrams(string: str, pattern: str) -> list:
    result_indices = []
    window_start, matched_char_num = 0, 0
    char_map = {}

    # Scan through pattern and create character to frequency map
    for char in pattern:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    
    # Begin sliding window
    # Our goal is to match all the characters from the 'char_map' with 
    # the current window.
    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in char_map:
            # Decrement the frequency of matched character
            char_map[right_char] -= 1
            if char_map[right_char] == 0:
                matched_char_num += 1
        
        # Have we found an anagram?
        if matched_char_num == len(char_map):
            result_indices.append(window_start)

        # Shrink the sliding window
        if window_end - window_start + 1 >= len(pattern):
            left_char = string[window_start]

            if left_char in char_map:
                if char_map[left_char] == 0:
                    # Before putting the character back, decrement the matched count
                    matched_char_num -= 1 
                char_map[left_char] += 1

                window_start += 1

    return result_indices


if __name__ == "__main__":
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))
    print(find_string_anagrams("cbaebabacd", "abc"))
    print(find_string_anagrams("abab", "ab"))