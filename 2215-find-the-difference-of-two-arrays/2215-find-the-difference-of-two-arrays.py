class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1={}
        dict2={}
        for i in nums1:
            if i not in dict1:
                dict1[i]=nums1.count(i)
        for i in nums2:
            if i not in dict2:
                dict2[i]=nums2.count(i)        
        list1=[i for i in dict1 if i not in dict2]
        list2=[i for i in dict2 if i not in dict1]
        return [list1,list2]
        