class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
    
        new_list=[]
        for i in range(int(len(nums)/2)):
            #freq = nums[2*(i)]
            #val = [nums[(2*i)+1]]
            #new_list = new_list+(freq * val)
            new_list = new_list + nums[2*(i)] * [nums[(2*i)+1]]
       
       return new_list
