class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        c = Counter(arr)
        b = set(arr)
        for key , val in c.items():
            if val == 1:
                res.append(key) 
        
        return res[k-1] if k-1 < len(res) else ""