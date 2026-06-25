class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0 
        sum = 0 
        for i in range(1,len(s)):
            sum+=abs(ord(s[i])-ord(s[i-1]))
        return sum