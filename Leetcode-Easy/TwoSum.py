class Solution:
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Storing indices of all integers in dictionary present in list
        a={}
        for i in range(len(nums)):
            a[nums[i]]=i
        
        result=[]
        #Getting the position of integers that add's up to target
        for i in range(len(nums)):
            c=target-nums[i]
            if c in a:
                if(a[c]>i):
                    result.append(i)
                    result.append(a[c])
                    return result
    
    
        
        


        
