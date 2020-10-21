"""
Sliding window - Longest Substring Without Repeating Characters (medium)
    
Description:
Given a string, find the length of the longest substring which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Time Complexity: O(N)
Space Complexity: O(K)

Leetcode Link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

def non_repeat_substring(string:str) -> int:
    window_start = 0
    max_len = 0
    window_map = {}

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in window_map:
            window_start = max(window_start, window_map[right_char] + 1)

        window_map[right_char] = window_end

        max_len = max(max_len, window_end-window_start+1)
    
    return max_len


if __name__ == "__main__":
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))