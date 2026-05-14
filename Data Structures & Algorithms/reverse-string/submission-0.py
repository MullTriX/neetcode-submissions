class Solution:
    def reverseString(self, s: List[str]) -> None:
        reverse = []
        i = len(s)-1
        while i>=0:
            reverse.append(s[i])
            i-=1
        for i in range(len(s)):
            s[i] = reverse[i]
        