class Solution:
    def isPossible(self,bloomDay:List[int],day:int,m:int,k:int)->bool:
        c=0
        ans=0
        for i in bloomDay:
            if i<=day:
                c=c+1
            else:
                ans=ans+ c//k
                c=0
        ans=ans+ c//k
        if ans>=m:
            return True
        else:
            return False
        
    def findMinMax(self,bloomDay:List[int])->List[int]:
        minimum=float('+inf')
        maximum=float('-inf')
        for i in bloomDay:
            minimum=min(i,minimum)
            maximum=max(i,maximum)
        return [minimum,maximum]  
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k > n:
            return -1
        low,high=self.findMinMax(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if self.isPossible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low        
        
        