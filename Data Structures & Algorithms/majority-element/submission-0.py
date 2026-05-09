class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            majority = nums.count(num)
            if majority > len(nums)/2:
                return num
        