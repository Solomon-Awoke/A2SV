class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return False
        x=sorted(arr)
        y=sorted(arr)[::-1]
        if arr==x or arr==y:
            return False
        ind=arr.index(max(arr))
        z=arr[:ind]
        w=arr[ind:]
        if z and w and z == sorted(z) and w == (sorted(w)[::-1]):
            return True
        return False