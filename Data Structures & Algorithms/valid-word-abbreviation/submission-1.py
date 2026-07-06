class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0 
        r = 0 
        while l < len(word) and r < len(abbr):
            if abbr[r].isalpha():
                if word[l] == abbr[r]:
                    l+=1
                    r+=1
                else:
                    return False
            while  r < len(abbr) and abbr[r].isalpha() == False:
                if abbr[r] == '0':
                    return False 
                num = ""
                while  r < len(abbr) and abbr[r].isalpha() == False:
                    num+=abbr[r]
                    r+=1
                l+=int(num)
        if l == len(word) and r == len(abbr):
            return True
        else:
            return False
