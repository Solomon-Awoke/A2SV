class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        k=len(mat)
        l=len(mat[0])
        if k*l != r*c:
            return mat
        out=[]
        put=[]
        m=[]
        p=0
        for i in mat:
            for j in i:
                m.append(j)
        for i in range(r):
            for j in range(c):
                out.append(m[p])
                p+=1
            put.append(out)
            out=[]
        return put