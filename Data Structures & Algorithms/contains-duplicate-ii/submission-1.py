class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        wind = set()
        for r in range(0,len(nums)):
            while r - l > k:
                wind.remove(nums[l])
                l+=1
            if nums[r] in wind:
                return True
            wind.add(nums[r])
        return False