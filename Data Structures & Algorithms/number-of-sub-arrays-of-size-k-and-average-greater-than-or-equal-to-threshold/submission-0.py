class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0 
        count = 0 
        for r in range(0,len(arr)):
            while r - l + 1 > k:
                l+=1
            if r - l + 1 == k:
                avg = sum(arr[l:r+1])//k 
                if avg >= threshold:
                    count+=1
        return count
        