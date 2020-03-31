class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        a=0
        for i in range(len(sorted_nums)):
            if i%2 ==0:
                a+=sorted_nums[i]
        
        return a
