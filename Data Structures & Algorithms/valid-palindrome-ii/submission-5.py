class Solution:
    def validPalindrome(self, s: str) -> bool:
        clear = ''.join(ch for ch in s if ch.isalnum()).lower()
        l = 0
        r = len(clear) - 1
        def palindrome(s,l,r, deleted):
            while l < r:
                if s[l] != s[r]:
                    if deleted:
                        return False
                    return palindrome(s, l+1, r, True) or palindrome(s, l, r-1, True)
                l+=1
                r-=1
            return True
        return palindrome(clear,l,r, False)