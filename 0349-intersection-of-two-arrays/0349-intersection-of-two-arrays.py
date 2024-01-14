class Solution:
    def binarySearch(self,list1:List[int],f:int)->bool:
        list1.sort()
        low=0
        high=len(list1)-1
        while low<=high:
            mid=(low+high)//2
            if list1[mid]==f:
                return True
            else:
                if list1[mid]>f:
                    high=mid-1
                else:
                    low=mid+1
        return False           
        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list=[]
        if len(nums1)<=len(nums2):
            list1=nums1
            list2=nums2
        else:
            list1=nums2
            list2=nums1
        for i in list1:
            if self.binarySearch(list2,i) ==True:
                if i not in list:
                    list.append(i)
        return list            
        