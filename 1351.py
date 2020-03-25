class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count=0
        for i in grid:
            count += (len(list(filter(lambda x: (x < 0), i))) )
        
        return count
