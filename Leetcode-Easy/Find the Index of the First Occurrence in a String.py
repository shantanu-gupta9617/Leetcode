class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(haystack)<len(needle)):
            return -1

        f=needle[0]
        
        for i in range(len(haystack)):
            if(f==haystack[i] and needle==haystack[i:i+len(needle)]):
                return i
        
        return -1
