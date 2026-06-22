class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = -1
        total = 0 
        for row in grid:
            for num in row:
                total+=num
                if num in seen:
                    repeated = num
                else:
                    seen.add(num)
        exp = (n*n) * (n*n+1) // 2
        miss = exp - (total - repeated)
        return [repeated,miss]