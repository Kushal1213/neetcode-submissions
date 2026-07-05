class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == [1]:
            return 2
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        return len(nums)+1