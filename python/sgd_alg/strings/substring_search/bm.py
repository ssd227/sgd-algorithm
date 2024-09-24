'''
Boyer-Moore


Property: 
    Substring search with the Boyer-Moore mismatched character
    heuristic takes about ~ N / M character compares to search
    for a pattern of length M 
    in a text of length N.
    
Worst-case:
    Can be as bad as ~ M N.
'''

class BM:
    def __init__(self, pat) -> None:
        self.pat = pat
        self.patc2rid = self.calc_rightmost() # dict[pattern_char][rightmost_id]
        
    # Precompute index of rightmost occurrence of character in pattern c
    def calc_rightmost(self):
        rightmost = dict()
        for i, c in zip(range(len(self.pat)), self.pat):
            rightmost[c] = i
        return rightmost

    def search(self, txt:str):
        n, m = len(txt), len(self.pat)
        
        i = skip = 0
        while(i<=(n-m)):
            skip = 0
            
            for j in range(0,m)[::-1]: # pattern 从右向左依次匹配 [m-1, m-2,.., 1, 0]
                if self.pat[j] != txt[i+j]:
                    txtc = txt[i+j]
                    if txtc not in self.patc2rid:
                        skip = -1
                    else:
                        skip = j-self.patc2rid[txtc]
                    skip = max(1, skip)
                    break
                
            if skip==0: return i # match
            i+= skip
        
        return n # not find
    