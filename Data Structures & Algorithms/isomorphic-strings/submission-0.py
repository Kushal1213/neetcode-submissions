class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        i= 0 
        while i < len(s):
            if (s[i] in st and st[s[i]] != t[i] ) or (t[i] in ts and ts[t[i]] != s[i]):
                return False
            else:
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
            i+=1
        return True