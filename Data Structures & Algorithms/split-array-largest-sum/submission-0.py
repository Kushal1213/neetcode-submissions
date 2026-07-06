class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l = max(nums)
        r = sum(nums)
        res = r 

        def a(mid):
            curr = mid
            s = 1
            for n in nums:
                if curr - n < 0:
                    curr = mid
                    s+=1
                curr=curr-n 
            return s <= k 
        

        while l <= r:
            mid = (l + r)//2
            if a(mid) == True:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res 


