class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    
        count=0
        for Jstr in J:
            for Sstr in S:
                    if (Jstr==Sstr):
                        count=count+1
        
        return count
