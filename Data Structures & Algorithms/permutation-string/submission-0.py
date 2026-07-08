class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        a = len(s1)
        l = 0
        for r in range(0,len(s2)):
            if r - l + 1 > a:
                l+=1
            
            if r - l + 1 == a:
                c2 = Counter(s2[l:r+1])
                if c2 == c:
                    return True
        return False 



