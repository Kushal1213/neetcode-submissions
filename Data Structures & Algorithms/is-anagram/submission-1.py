class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:

            hs = {}
            ht = {}
            for i in s:
                hs[i] = 1 + hs.get(i,0)
            for j in t:
                ht[j] = 1 + ht.get(j,0)
            for ch in hs:
                if hs[ch] !=  ht.get(ch,0):
                    return False
            return True