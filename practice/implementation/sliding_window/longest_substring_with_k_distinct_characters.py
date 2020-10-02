"""
Sliding window - Longest Substring with K Distinct Characters (medium)

Description:
Given a string, find the length of the longest substring 
in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Time Complexity - O(N)
Space Complexity - O(1)

LeetCode link: https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""

def longest_substring_with_k_distinct(string, k):
    window_start = 0
    maximum_length = 0
    char_set = set()

    for window_end in range(len(string)):
        char_set.add(string[window_end])
        
        while len(char_set) > k:
            window_start += 1
            char_set = set(string[window_start:window_end+1])
        
        maximum_length = max(maximum_length, window_end-window_start+1)
        
        print(string[window_start:window_end+1])    
        print(char_set)
        print(maximum_length)
    return maximum_length


if __name__=="__main__":
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("aa", 3)))