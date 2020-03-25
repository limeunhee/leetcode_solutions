class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:        
        new_list = [i for x in grid for i in x]
        return sum([num<0 for num in new_list])
