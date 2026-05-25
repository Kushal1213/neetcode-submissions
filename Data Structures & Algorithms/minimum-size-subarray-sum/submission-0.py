class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        res = 10000
        total = 0 
        for r in range(0,len(nums)):
            total+=nums[r]
            while total>=target:
                res = min(r-l+1,res)
                total-=nums[l]
                l+=1
        if res == 10000:
            return 0
        else:
            return res
