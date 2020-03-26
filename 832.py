class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        new_list=[]
        for image in A:
            new_image=[]
            for j in range(-1,-(len(image)+1),-1):
                if image[j]==0:
                    new_image.append(image[j]+1)
                else:
                    new_image.append(image[j]-1)
            new_list.append(new_image)
            
        return (new_list)
