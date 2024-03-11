class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        d=n-2
        suffix_max=[arr[n-1]]
        j=0
        while d>=0:
            suffix_max.append(max(arr[d],suffix_max[j]))
            d-=1
            j+=1
        for i in range(n):
            if i==n-1:
                arr[i]=-1
            else:    
                arr[i]=suffix_max[n-2-i]
        return arr    