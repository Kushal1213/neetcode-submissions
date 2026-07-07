class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total+=n
            self.prefix.append(total)


        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 :
            prefixl = self.prefix[left-1]
        else:
            prefixl = 0
        prefixr = self.prefix[right]
        res = prefixr - prefixl 
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)