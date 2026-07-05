class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0 
        res = float('inf')
        for r in range(0,len(nums)):
            while r- l + 1 > k:
                l+=1
            if r - l + 1 == k :
                mn = min(nums[l:r+1])
                mx = max(nums[l:r+1])
                rs = mx - mn 
                res = min(res,rs)
        return res


        