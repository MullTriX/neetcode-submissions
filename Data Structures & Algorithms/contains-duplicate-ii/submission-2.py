class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = False
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] == nums[j]:
                    if abs(i-j) <= k:
                        store = True
        return store