class Solution:
    def dayCalculator(self,weights:List[int],w:int)->int:
        n=len(weights)
        s=0
        days=1
        for i in range(n):
            if  s+weights[i]>w:
                     s=weights[i]
                     days+=1
            else:
                    s=s+weights[i]
        return days        
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=0
        for i in weights:
            low=max(low,i)
        high=sum(i for i in weights)
        while low<=high:
            mid=(low+high)//2
            if self.dayCalculator(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
                
        return low    
            
        