class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
        while L <= R:
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            L+=1
            R-=1
        return -1