class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x
        
        left = 1
        right = x//2 +1
        mid = (left+right)//2
        
        while left<right-1:
            
            if mid**2 == x:
                return mid
            if mid**2 > x:
                right = mid
            elif mid**2 <x:
                left = mid   
            mid = (left+right)//2
        return mid
