class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0 
        p = 1
        res = 0 
        if k <=1:
            return 0
        for r in range(0,len(nums)):
            p*=nums[r]
            while p >= k :
                p = p // nums[l]
                l+=1
            if p < k:
                res+=r-l+1
        return res
