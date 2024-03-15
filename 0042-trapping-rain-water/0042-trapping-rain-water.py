class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        pm=[arr[0]]
        sm=[arr[n-1]]
        j=0
        k=0
        for i in range(1,n):
            pm.append(max(pm[j],arr[i]))
            j+=1
        for i in range(n-2,-1,-1):
            sm.append(max(sm[k],arr[i]))
            k+=1
            
        ans=0
        for i in range(1,n-1):
                ans+=min(sm[n-1-i],pm[i])-arr[i]    
            
        return ans
        