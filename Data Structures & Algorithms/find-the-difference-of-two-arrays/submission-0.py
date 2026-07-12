class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        resa =[]
        resb = []
        a = set(nums1)
        b = set(nums2)

        for i in a:
            if i not in b:
                resa.append(i)
        
        for i in    b:
            if i not in a:
                resb.append(i)

        return [resa,resb]
