"""
Sliding window - Longest Substring With Same Letters after Replacement (hard)

Description:
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Time Complexity: O(N)
Space Complexity: O(1)

Leetcode Link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

def length_of_longest_substring(string:str, k:int) -> int:
    window_start = 0
    frequency_dict = {} # Record frequency of letters in the current window
    max_repeat_letter_count = 0 # Maximum repeating letter count 
    max_length = 0 # Maximum length (output)

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char not in frequency_dict:
            frequency_dict[right_char] = 0
        frequency_dict[right_char] += 1

        max_repeat_letter_count = max(max_repeat_letter_count, frequency_dict[right_char])

        # Shrink the window whence the window size minus the max_repeat_letter_count is more than
        # 'k', since we are not allowed to replace more than 'k' letters.
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = string[window_start]
            frequency_dict[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

if __name__ == "__main__":
    print(f"Length of the longest substring: {length_of_longest_substring('aabccbb', 2)}")
    print(f"Length of the longest substring: {length_of_longest_substring('abbcb', 1)}")
    print(f"Length of the longest substring: {length_of_longest_substring('abccde', 1)}")
    print(f"Length of the longest substring: {length_of_longest_substring('abccde', 2)}")