class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        hasht = {}
        for i in s:
            hashs[i] = 1 + hashs.get(i, 0)
        for j in t:
            hasht[j] = 1 + hasht.get(j, 0)
        
        for c in hashs:
            if hashs[c] != hasht.get(c, 0):
                return False
        return True