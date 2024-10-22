class Solution:
    def isPalindrome(self, n: int) -> bool:
        
        #Negative numbers cannot be Palindrom for example -121 reverse is 121-
        if n<0:
            return False
        
        return str(n)==str(n)[::-1]


        
