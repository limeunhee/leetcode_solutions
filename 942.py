class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        a=0
        b=len(S)
        n_list=[]
        
        for i in range(len(S)):
            print(S[i])
            if S[i]=="I":
                n_list.append(a)
                a+=1
            else:
                n_list.append(b)
                b-=1        
        n_list.append(a)
        
        return n_list
