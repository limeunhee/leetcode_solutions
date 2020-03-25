class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        n=""
        i = len(s)-1
        while i >-1:
            if s[i]=='#':
                n=chr(int(s[i-2]+s[i-1])+96) +n
                i = i-3
            else:
                n=chr(int(s[i])+96) +n
                i = i-1
        
        return n
