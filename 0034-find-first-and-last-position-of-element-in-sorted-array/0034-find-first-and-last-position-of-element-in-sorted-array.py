class Solution:
    def findFirst(self,nums:List[int],target:int)-> int: 
        # kind of like lower bound with equality necessary
        low=0
        high =len(nums)-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
    def findLast(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                ans = mid  
                low = mid + 1  
            else:
                high = high - 1
        return ans
    
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        ans1=self.findFirst(nums,target)
        ans2=self.findLast(nums,target)
        if nums[ans1] !=target:
            ans1=-1
        if nums[ans2] !=target:
            ans2=-1
        return [ans1,ans2]    
            
        
        