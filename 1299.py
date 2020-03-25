class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = [max(arr[i+1:]) for i in range(len(arr)-1)]
        new.append(-1)
        return new

