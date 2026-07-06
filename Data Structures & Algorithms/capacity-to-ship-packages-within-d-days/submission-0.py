class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = sum(weights)

        def can(mid):
            ship  = 1
            curr = mid
            for w in weights:
                if curr-w < 0:
                    ship+=1
                    curr = mid
                curr-=w
            return ship <= days

        while l <= r:
            mid = (l+r)//2
            if can(mid) == True:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        return res
            
        
        