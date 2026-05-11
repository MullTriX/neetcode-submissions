class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = k * [0]
        i=0
        prev=0
        while i < k:
            for num in nums:
                n = nums.count(num)
                if num not in frequent:
                    if prev < n:
                        frequent[i] = num
                        prev = n
                    prev-=1
            i+=1
        return frequent
