class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0 
        ws = 0 
        count = 0 
        for r in range(0,len(arr)):
            ws+=arr[r]
            if r - l + 1>k:
                ws-=arr[l]
                l+=1
            if r - l + 1 == k:
                avg = ws // k
                if avg >= threshold:
                    count+=1
        return count