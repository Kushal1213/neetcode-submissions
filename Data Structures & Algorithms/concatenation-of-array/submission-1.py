class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,2):
            for j in range(0,len(nums)):
                ans.append(nums[j])
        return ans