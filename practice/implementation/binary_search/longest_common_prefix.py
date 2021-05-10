"""
Binary Search / Divide & Conquer - Longest Common Prefix (easy)

Description:
Write a function to find the longest common prefix string amongst an 
array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

LeetCode: https://leetcode-cn.com/problems/longest-common-prefix
"""


def longest_prefix(strs: list) -> str:
    """ Scanning Column by Column

    Longest Common Prefix (LCP)

    Iterate throught the characters in the first string and compare 
    the character with all the remaning strings, if there is one 
    string not the same, then return the current LCP. Otherwise, 
    continue scanning and add the longest common index by 1.

    Time Complexity - O(M*N) - M is the average length of strings in 
    the array, N is the number of strings.
    Space Complexity - O(1) - Constant space.
    """
    # Edge cases
    if not strs: return ""

    # Length of the first string.
    length = len(strs[0])
    # Count the number of common characters.
    common_count = 0

    for i in range(length):
        char = strs[0][i]
        # Check if the character exist and it's the same on the 
        # same position.
        for string in strs:
            # i is beyond the length of current string or
            # string[i] is not the char from the first string.
            if i > len(string) - 1 or string[i] != char:
                return strs[0][:common_count]
        common_count += 1

    # If it doesn't return during the for loop, then the common
    # sub-string will be as long as the first string strs[0].
    return strs[0]


def longest_prefix_bs(strs: list) -> str:
    """ Binary Search

    Longest Common Prefix (LCP)

    The length of LCP will not exceed the length of the shortest 
    string in the list. We can use min_length to prepresent the length
    of the shortest string, and we can using binary search to search 
    in the range of [0, min_length] to find LCP.

    Each time, we take the middle value mid, and check whether the 
    prefix until mid are common, if yes, then the LCP shall be longer 
    or equal to mid, otherwise, the length of LCP shall be smaller than 
    mid. So we can update mid and search for LCP.

    Time Complexity - O(M*N*log(M)) - M is the minimum length of strings, 
    N is the number of strings. For binary search, each time we reduce 
    half, so the time complexity is O(logM), we at most iterate M*N 
    characters, so in total O(M*N*log(M)).
    Space Complexity - O(1) - Constant space.
    """
    # Edge cases
    if not strs: return ""

    def check_common_prefix(length):
        """ Check is until length is LCP. """
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count)) 

    # Get the min length of strings in the list.
    min_length = min(len(s) for s in strs)
    low, high = 0, min_length

    while low < high:
        # Update mid
        mid = (high - low + 1) // 2 + low
        
        if check_common_prefix(mid):
            # LCP shall be longer or equal.
            low = mid
        else:
            # LCP shall be shorter
            high = mid - 1 

    return strs[0][:low]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(f"Longest Common Prefix: {longest_prefix(strs)}")
    print(f"Longest Common Prefix: {longest_prefix_bs(strs)}")

    strs = ["dog","racecar","car"]
    print(f"Longest Common Prefix: {longest_prefix(strs)}")
    print(f"Longest Common Prefix: {longest_prefix_bs(strs)}")