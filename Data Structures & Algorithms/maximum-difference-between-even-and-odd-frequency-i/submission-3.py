class Solution:
    def maxDifference(self, s: str) -> int:
        odd = []
        even = []

        c = Counter(s)

        for val , key in c.items():
            if key % 2 == 0 :
                even.append(key)
            else:
                odd.append(key) 
        
        a = max(odd)

        d = min(even)

        return a - d
        