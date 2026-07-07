class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        e = 0 
        o = 1
        for num in nums:
            if num > 0 :
                res[e] = num 
                e+=2
            else:
                res[o] = num
                o+=2
        return res
        

        