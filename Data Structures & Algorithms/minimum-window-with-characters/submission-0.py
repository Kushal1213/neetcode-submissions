class Solution:
    def minWindow(self, s: str, t: str):
        if t == "":
            return ""

        ht = {}
        for c in t:
            ht[c] = 1 + ht.get(c, 0)

        want = len(ht)
        have = 0

        hs = {}
        l = 0

        res = [-1, -1]
        resl = float("inf")

        for r in range(len(s)):
            hs[s[r]] = 1 + hs.get(s[r], 0)

            if s[r] in ht and hs[s[r]] == ht[s[r]]:
                have += 1

            while have == want:

                if r - l + 1 < resl:
                    res = [l, r]
                    resl = r - l + 1

                hs[s[l]] -= 1

                if s[l] in ht and hs[s[l]] < ht[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resl != float("inf") else ""