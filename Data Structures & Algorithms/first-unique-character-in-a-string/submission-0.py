class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = Counter(s)
        for i , s in enumerate(s):
            if h[s] == 1:
                return i 
        return -1