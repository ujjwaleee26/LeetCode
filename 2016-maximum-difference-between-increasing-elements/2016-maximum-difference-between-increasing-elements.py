class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        least=nums[0]
        n=len(nums)
        for j in range(1,n):
            if nums[j]>least:
                ans=max(ans,nums[j]-least)
            least=min(least,nums[j])    
        return ans