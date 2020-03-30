class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n_list=[]
        for i in range(left,right+1,1):
            for ch in str(i):
                if int(ch)==0 or (i%int(ch))!=0:
                    break
            else:
                n_list.append(i)
        
        return n_list
