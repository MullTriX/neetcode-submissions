class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                mem = 0
                if nums[i] < nums[j]:
                    mem = nums[i]
                    nums[i] = nums[j]
                    nums[j] = mem
        return nums
        