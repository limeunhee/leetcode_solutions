class Solution:
    def sumZero(self, n: int) -> List[int]:
        if (n%2==1):
            return [*range(int(-n/2),int(n/2+1),1)]
        else:
            return [*range(int(-n/2),0,1),*range(1,int(n/2+1),1)]
