class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        for i in range(len(A)):
            if (A.count(A[i])) == (len(A)/2):
                return A[i]
