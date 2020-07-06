class Solution:
    def countAndSay(self, n: int) -> str:
        
        seq = "1"
        
        for i in range(1,n):    
            current = None
            count =0
            newseq=""
            
            for j in range(len(seq)):
                if seq[j] == current:
                    count +=1
                else:
                    if current:
                        newseq += str(count) + str(current)
                    
                    current = seq[j]
                    count = 1
            
            newseq += str(count) +str(current)
            seq = newseq
            
        return seq
    
            
