Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def longestCommonPrefix(self, strs: List[str]) -> str:
...         
...         ans=""
... #Calculating the minimum length of string present in the list
...         min_len=len(strs[0])
...         for i in range(len(strs)):
...             min_len=min(min_len,len(strs[i]))
... 
... 
... #Finding longest common prefix        
...         for i in range(min_len):
...             #s=""
...             ch=strs[0][i]
...             for j in range(len(strs)):
...                 if strs[j][i]==ch:
...                     continue
...                 else:
...                     return ans
...             ans=ans+ch
...         return ans
