import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_txt = ''.join(ch for ch in s if ch not in string.punctuation)
        clean_txt = clean_txt.lower().replace(" ", "")
        l = 0
        r = len(clean_txt) - 1
        while l < r:
            if clean_txt[l] != clean_txt[r]:
                return False
            l+=1
            r-=1
        return True