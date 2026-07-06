class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0 
        for r in range(0,len(nums)):
            if nums[r] != 0 :
                nums[k] = nums[r]
                k+=1
        while k < len(nums):
            nums[k] = 0 
            k+=1