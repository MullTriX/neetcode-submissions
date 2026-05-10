class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, start, end):
            mid = (start + end) // 2
            nums[mid], nums[end] = nums[end], nums[mid]
            pivot = nums[end]
            i = start - 1

            for j in range(start, end):
                if nums[j] <= pivot:
                    i+=1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[end] = nums[end], nums[i+1]
            return i + 1
        def quickSort(nums, start=0, end=None) -> List[int]:
            if end is None:
                end = len(nums)-1
            
            if start < end:
                pivot = partition(nums, start, end)
                quickSort(nums, start, pivot-1)
                quickSort(nums, pivot+1, end)
            return nums
        return quickSort(nums)
        

            
        