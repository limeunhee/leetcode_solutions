class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen=dict()
        
        for i in range(len(arr)):
            if arr[i] in seen.keys():
                seen[arr[i]] +=1
            else:
                seen[arr[i]] =1
    
        return len(seen) == len(set(seen.values()))
