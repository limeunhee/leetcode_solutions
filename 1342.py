import numpy as np

class Solution:
    def numberOfSteps (self, num: int) -> int:
              
        a=num
        count = 0
        
        while a != 0:
            if (a%2)==0:
                a = a/2
                count = count +1
            elif (a%2)==1:
                a= a-1
                count = count +1
        
        return count

