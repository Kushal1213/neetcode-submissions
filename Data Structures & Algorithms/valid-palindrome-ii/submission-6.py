class Solution:
    def validPalindrome(self, s: str) -> bool:
        a = 0 
        b = len(s) - 1
        while a <= b:
            if s[a] != s[b] :
                skipl = s[a+1:b+1]
                skipr = s[a:b]
                return (skipl == skipl[::-1]or skipr==skipr[::-1])
            a+=1
            b-=1
        return True
