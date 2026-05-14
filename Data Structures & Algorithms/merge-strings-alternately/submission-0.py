class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        maxLength = max(len(word1), len(word2))
        i = 0
        while i < maxLength:
            if i < len(word1):
                merged+=(word1[i])
            if i < len(word2):
                merged+=(word2[i])
            i+=1
        return merged
