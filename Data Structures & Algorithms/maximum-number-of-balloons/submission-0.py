class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter("balloon") 
        res = float('inf')
        b = Counter(text)

        for i in c :
            res= min(res,b[i]//c[i]) 
        
        return res