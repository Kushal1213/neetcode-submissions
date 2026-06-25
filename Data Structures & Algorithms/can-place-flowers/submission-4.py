class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = [0] + flowerbed + [0]
        count = 0

        for i in range(1, len(s)-1):
            if s[i] == 0 and s[i-1] == 0 and s[i+1] == 0:
                s[i] = 1      # plant the flower
                count += 1

        return count >= n