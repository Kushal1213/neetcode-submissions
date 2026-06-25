class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = Counter(nums)
        res = 0 
        for n , c in h.items():
            res+=(c*(c-1))//2
        return res