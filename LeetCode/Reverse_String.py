class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k=len(s)
        for i in range (k-1,-1,-1):
            s.append(s[i])
        for i in range(k):
            s.remove(s[i])