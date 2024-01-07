class Solution(object):
    def missingNumber(self, nums):
        ce=len(nums)
        return (ce*(ce+1))/2-sum(nums)
        