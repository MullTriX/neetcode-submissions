class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = False
        for i in range(len(nums)):
            for j in range(1, k+1):
                if i + j < len(nums) and nums[i] == nums[i+j]:
                    return True
        return False