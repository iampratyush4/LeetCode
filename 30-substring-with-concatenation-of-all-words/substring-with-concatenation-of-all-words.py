from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []
        
        # Loop through the string s up to the last possible starting index
        for i in range(len(s) - total_length + 1):
            seen = {}
            j = 0
            # Check words in the substring starting at index i
            while j < num_words:
                word_start = i + j * word_length
                word = s[word_start: word_start + word_length]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    # If a word is seen more times than it appears in words, break early
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            # If we managed to match all words, record the starting index
            if j == num_words:
                result.append(i)
                
        return result

