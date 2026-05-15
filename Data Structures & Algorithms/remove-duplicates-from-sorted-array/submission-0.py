class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        i = len(nums) - 1
        while i >= 0:
            if nums[i] in seen:
                nums.remove(nums[i])
            seen.append(nums[i])
            i-=1
        print(nums)
        return len(seen)
            
        