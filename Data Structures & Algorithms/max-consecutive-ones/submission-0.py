class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0 
        mc = 0 
        i = 0 
        while i < len(nums):
            if nums[i] == 0 :
                c = 0 
            else:
                c+=1
                mc = max(mc,c)
            i+=1
        return mc