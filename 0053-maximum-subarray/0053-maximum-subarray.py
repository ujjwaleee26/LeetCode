class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float('-inf')
        sum=0
        for i in nums:
            sum=sum+i
            ans=max(ans,sum)
            if sum<0:
                sum=0
        return ans        
        