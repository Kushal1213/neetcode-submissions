class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)

        res = []

        for num in nums1 :
            nextGreater = - 1
            for i in reversed(nums2):
                if i > num:
                    nextGreater = i 
                elif i == num :
                    break
            res.append(nextGreater) 
        return res