class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cw = 0 
        l = 0 
        mino = float('inf')
        for r in range(0,len(blocks)):
            if r - l + 1 > k:
                if blocks[l] == 'W':
                    cw-=1
                l+=1
            if blocks[r] == 'W':
                cw+=1
            if r - l + 1 == k :
                mino = min(mino,cw)
        return mino

        