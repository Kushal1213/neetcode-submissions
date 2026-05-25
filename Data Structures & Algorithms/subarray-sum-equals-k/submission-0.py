class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currentsum = 0 
        h = {0 : 1}
        for n in nums:
            currentsum+=n
            diff = currentsum - k 
            res+=h.get(diff,0)
            h[currentsum] = 1 + h.get(currentsum,0)
        return res
        