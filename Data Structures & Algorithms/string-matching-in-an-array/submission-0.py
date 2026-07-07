class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        res = []
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

