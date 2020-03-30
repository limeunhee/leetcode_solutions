class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [num*num for num in A]
        A.sort()
        return A
