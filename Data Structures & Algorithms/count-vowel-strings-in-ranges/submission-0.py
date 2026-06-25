class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []

        for li, ri in queries:
            cnt = 0
            for word in words[li:ri+1]:
                if word[0] in vowels and word[-1] in vowels:
                    cnt += 1
            ans.append(cnt)

        return ans