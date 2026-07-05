class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 
        h = {}
        res = 0
        maxres = 0
        for r in range(0,len(fruits)):
            h[fruits[r]] = 1 + h.get(fruits[r],0)
            while len(h) > 2:
                h[fruits[l]] = h.get(fruits[l],0)-1
                if h[fruits[l]] == 0 :
                    del h[fruits[l]]
                l+=1
            if len(h)<=2:
                res=sum(h.values())
                maxres = max(maxres,res)
        return maxres
