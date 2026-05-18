class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            left=sum(nums[0:i])
            right = sum(nums) - left - nums[i]
            if left == right:
                return i 
        return -1
        