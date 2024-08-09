class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return [-1]
        out=[-1]
        val=-1
        for i in range(len(arr)-1,0,-1):
            out.append(max(arr[i],val))
            val=(max(arr[i],val))
        return out[::-1]