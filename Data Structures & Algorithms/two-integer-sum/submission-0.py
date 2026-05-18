class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i , n in enumerate(nums):
            comp = target - n
            if comp in h:
                return [h[comp],i]
            h[n] = i 
        return 