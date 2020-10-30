"""
Sliding window - Words Concatenation (hard)

Description:
Given a string and a list of words, find all the starting indices of substrings 
in the given string that are a concatenation of all the given words exactly once 
without any overlapping of words. It is given that all words are of the same length.

Example: 
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Notes:
1. Words could repeat in the words list.
2. Words are all of the same length.
3. The word order in the substring doesn't matter.

Time Complexity - O(N * M * Len)
Space Complexity - O(M+N), O(M) for storing all the words in two hash maps, while in 
the worst case, the result list will take place of O(N).
where:
 - N is the number of characters in the given input string.
 - M is the total number of words in the given words list.
 - Len is the length of a word.

LeetCode link: https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
"""


def find_concatenation_substring(string: str, words: list) -> list:
    # Edge cases: empty words list or word is empty string.
    if len(words) == 0 or len(words[0]) == 0:
        return []

    result_indices = []
    word_map = {}
    word_len = len(words[0])
    words_num = len(words)

    # Scan words list and get the frequency map.
    for word in words:
        if word not in word_map:
            word_map[word] = 0
        word_map[word] += 1
    
    # Start from 0 to (len(string) - word_len * words_num) + 1
    # since the window length is fixed to word_len * words_num.
    for i in range((len(string) - word_len * words_num) + 1):
        words_seen = {}
        # Scan through words in the window as the word length is fixed.
        for j in range(0, words_num):
            # Get the next word's index and text.
            word_index = i + j * word_len
            word = string[word_index: word_index+word_len]

            # Break if we don't see this word in the provided words list.
            if word not in word_map:
                break
            
            # Add the word to the words_seen map.
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word frequency in the window
            # is higher than required (in the words list frequency map).
            if words_seen[word] > word_map.get(word, 0):
                break
            
            # Store index since we've already found all the words.
            if j + 1 == words_num:
                result_indices.append(i)

    return result_indices


if __name__ == "__main__":
    print(find_concatenation_substring("catfoxcat", ["cat", "fox"]))
    print(find_concatenation_substring("catcatfoxfox", ["cat", "fox"]))
    print(find_concatenation_substring("barfoothefoobarman", ["foo", "bar"]))
    print(find_concatenation_substring("wordgoodgoodgoodbestword", ["word","good","best","word"]))


