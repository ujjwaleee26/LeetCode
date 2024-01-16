class Solution:
    def divSum(self,nums:List[int],divisor:int)->int:
        sum=0
        for i in nums:
            sum=sum+ ceil(i/divisor)
        return sum    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans=0
        for i in nums:
            ans=max(ans,i)
        low=1
        high=ans    
        while low<=high:
            mid=(low+high)//2
            if self.divSum(nums,mid)<=threshold:
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans     
        