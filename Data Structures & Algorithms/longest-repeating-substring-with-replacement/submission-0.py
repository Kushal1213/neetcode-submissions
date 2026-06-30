class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0 
        res = 0 
        for r in range(0,len(s)):
            h[s[r]] = 1 + h.get(s[r],0)
            while (r-l) - max(h.values()) >= k:
                h[s[l]] = h.get(s[l],0) - 1
                l+=1
            res = max(res,r-l+1)
        return res