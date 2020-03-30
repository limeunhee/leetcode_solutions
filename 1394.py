class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=-1
        for i in range(len(arr)):
            if (arr[i]>a) and (arr[i] ==arr.count(arr[i])):
                    a= arr[i]
        return a
