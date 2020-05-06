class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if target/2 in nums:
            indices = [i for i, x in enumerate(nums) if x == target/2]
            if len(indices)>1:
                return [indices[0],indices[1]]
            else:
                diff = [target - x for x in nums]
                a = list(set(nums) & set(diff))
                a.remove(target/2)
                return [nums.index(a[0]),nums.index(a[1])]   
        else:
            diff = [target - x for x in nums]
            a = list(set(nums) & set(diff))
            return [nums.index(a[0]),nums.index(a[1])]        
   
