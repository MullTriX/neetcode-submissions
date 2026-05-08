class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return prefix
            prefix += shortest[i]
        return prefix