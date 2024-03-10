class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod=1
        l=0
        ans=0
        n=len(nums)
        for r in range(n):
            prod*=nums[r]
            while prod>=k  and l<=r:
                prod=prod//nums[l]
                l+=1
            ans+=(r-l+1)    
        return ans    