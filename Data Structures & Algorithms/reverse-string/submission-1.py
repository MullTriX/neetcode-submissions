class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s)-1
        while r > l:
            s[r], s[l] = s[l], s[r]
            l+=1
            r-=1
        print(s)
        