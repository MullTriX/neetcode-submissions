class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = [[] for i in range(k)]
        i=0
        prev=0
        while i < k:
            for num in nums:
                n = nums.count(num)
                if num not in frequent:
                    if prev < n:
                        frequent[i] = num
                        prev = n
            for num in nums:
                if num in frequent:
                    nums.remove(num)
            print(nums)
            prev=0
            i+=1
        return frequent