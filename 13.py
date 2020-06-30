class Solution:
    def romanToInt(self, s: str) -> int:

        sum_=0
        
        substrs1= {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        substrs2 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
        for key,value in substrs1.items():
            if key in s:
                sum_+= substrs1[key]    
                s=s.replace(key,'')
        
        for item in s:
            sum_ += substrs2[item]
        
        return (sum_)
