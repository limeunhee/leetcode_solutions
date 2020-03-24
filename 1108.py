class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        new_str=""
        for str in address:
            if str=='.':
                new_str = new_str+ "[.]"
            else:
                new_str=new_str+str
        
        return (new_str)
