class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in range(len(strs)):
            mem = []
            for s in strs:
                if sorted(strs[i]) == sorted(s):
                    mem.append(s)
            if mem not in res:
                res.append(mem)
        return res