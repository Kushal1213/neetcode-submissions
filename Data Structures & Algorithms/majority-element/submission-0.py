class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        res = 0 
        maxcount = 0 
        for n in nums:
            h[n] = 1 + h.get(n,0)
            if h[n] > maxcount:
                res = n 
            else:
                res
            maxcount = max(h[n],maxcount)
        return res
             


        