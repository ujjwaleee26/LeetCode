class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tempDict={}
        lst=[]
        for i in nums:
            if i not in tempDict:
                tempDict[i]=nums.count(i)
        nums.clear()
        for key in tempDict:
            nums.append(key)
        return len(tempDict) 
        