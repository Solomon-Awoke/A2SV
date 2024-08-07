class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            words[i] = ''.join(sorted(list(set(words[i]))))
        mydict={}
        for i in words:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        out = 0
        for i in mydict.values():
            if i > 1:
                out += (i * (i - 1)) // 2  
        
        return out