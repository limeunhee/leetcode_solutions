class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        out = collections.Counter()
        
        for items in cpdomains:
            n,s = items.split()
            n= int(n)
            
            frags = s.split('.')
            for i in range(len(frags)):
                out[".".join(frags[i:])] += n
            
        return [f'{ct} {dom}' for dom,ct in out.items()]
