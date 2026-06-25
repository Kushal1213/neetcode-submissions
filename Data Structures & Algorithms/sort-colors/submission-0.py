class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr =[0]*3
        for i in nums:
            arr[i]+=1
        k = 0 
        for i in range(0,len(arr)):
            while arr[i] > 0:
                nums[k] = i
                arr[i]-=1
                k+=1
        