class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        while k>n:
            k-=n
        l1=nums[n-k:]
        l2=nums[:n-k]
        nums[:]=nums[n-k:]+nums[:n-k]

        
        