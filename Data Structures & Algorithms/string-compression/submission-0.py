class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0 
        k = 0 
        n = len(chars)

        while l < n:
            chars[k] = chars[l]
            k+=1
            j = l + 1
            while j < n and chars[j] == chars[l]:
                j+=1
            if j - l > 1:
                d = str(int(j)-int(l))
                for digits in d:
                    chars[k] = digits
                    k+=1
            l = j
        return k
