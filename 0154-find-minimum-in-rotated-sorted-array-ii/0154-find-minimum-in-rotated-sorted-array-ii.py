class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=6000
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]==nums[mid]==nums[high]:
                ans=min(ans,nums[low])
                low=low+1
                high=high-1
                continue
            if low<len(nums) and high<len(nums):    
                if nums[low]<=nums[mid]:
                    ans=min(ans,nums[low])
                    low=mid+1
                else:
                    ans=min(ans,nums[mid])
                    high=high-1
            if low==high:
                ans=min(ans,nums[low])
                break
        return ans    
        