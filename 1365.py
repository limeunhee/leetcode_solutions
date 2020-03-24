class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        small_count =[]
        for i in range(len(nums)):
            a= nums[i]
            diff = [a - x for x in nums]
            b = [x > 0 for x in diff]
            small_count.append((b.count(True)))
        
        return (small_count)
