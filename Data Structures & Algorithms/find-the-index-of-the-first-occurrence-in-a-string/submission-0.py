class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        for i in range(0,a-b+1):
            for j in range(0,b):
                if haystack[i+j] != needle[j]:
                    break 
                if j == b-1:
                    return i 
        return - 1