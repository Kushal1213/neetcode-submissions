class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        resm = 0
        total = 0 
        l = 0 
        for r in range(0,len(nums)):
            total+=nums[r]

            while nums[r]*(r-l+1) > total+k:
                total-=nums[l]
                l+=1

            if nums[r]*(r-l+1) <= total+k:
                res = r- l + 1
                resm = max(resm,res)
            
            
            
        return resm

            

