class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        word=""
        for i in range(len(haystack)):
            word= word+ haystack[i]

            if word == needle:
                return i- len(needle) + 1
            if len(word)== len(needle):
                word=word[1:]
        return -1