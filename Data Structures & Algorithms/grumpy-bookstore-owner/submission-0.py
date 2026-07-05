class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0 
        sat = 0 
        a = 0 
        maxr = 0 
        for r in range(0,len(customers)):
            if grumpy[r] == 1:
                a+=customers[r]
            else:
                sat+=customers[r]
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    a-=customers[l]
                l+=1
            maxr = max(maxr,a)
        return maxr+sat