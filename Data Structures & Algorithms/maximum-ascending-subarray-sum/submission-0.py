class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        maxres = nums[0] 
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1] :
                res+=nums[i]
                maxres = max(maxres , res)
            else :
                res = nums[i]
            i+=1
        return maxres