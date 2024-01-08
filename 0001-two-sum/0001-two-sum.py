class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for key,value in enumerate(nums):
            complement = target - value
            if complement in dict:
                return [dict[complement], key]
            dict[value] = key

        return []  # No solution found

            
         
                    
        