import numpy as np 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        list = [int(x) for x in str(n)]
        sums= sum(list)
        products = np.prod(list)
        
        return products-sums
