class Solution:
    def balancedStringSplit(self, s: str) -> int:
    
        total_count=0
        r_count=0
        l_count=0
        for i in s:
            if i=="R":
                r_count = r_count+1
            else:
                l_count = l_count+1

            if r_count == l_count:
                total_count = total_count+1
       
       return total_count   
