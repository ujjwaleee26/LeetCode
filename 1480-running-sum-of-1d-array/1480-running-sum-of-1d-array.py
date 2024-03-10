class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=0
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]+nums[j]
            j+=1
            
        return nums    
        