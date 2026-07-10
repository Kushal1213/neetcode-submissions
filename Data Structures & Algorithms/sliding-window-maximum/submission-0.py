class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0 

        for r in range(0,len(nums)):
            if r>=k:
                l+=1
            if r>=k-1:
                res.append(max(nums[l:r+1]))
        return res