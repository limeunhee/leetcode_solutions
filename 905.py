class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        new_list=[]
        for i in A:
            if (i%2==0):
                new_list.insert(0,i)
            else:
                new_list.append(i)
        
        return new_list
