class Solution:
    def maxElement(self,piles:List[int])->int:
        ans=float(-inf)
        for i in piles:
            ans=max(ans,i)
        return ans 
    def hourCalc(self,piles:List[int],k:int):
        s=0
        for i in piles:
            s=s+ ceil(i/k)
        return s    
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=self.maxElement(piles)
        while low<=high:
            mid=(low+high)//2
            hours=self.hourCalc(piles,mid)
            if hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low        
        
        
        