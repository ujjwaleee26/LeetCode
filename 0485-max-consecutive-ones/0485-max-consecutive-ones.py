class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr=[]
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                arr.append(count)
                count=0
        if count !=0:        
            arr.append(count)        
        arr.sort()
        return arr.pop()
                
        