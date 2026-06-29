class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        res = 0 
        ans = float('inf')
        for r in range(0,len(nums)):
            res+=nums[r]
            while res>= target:
                ans = min(ans,r-l+1)
                res-=nums[l]
                l+=1
        if ans == float('inf'):
            return 0
        else:
            return ans