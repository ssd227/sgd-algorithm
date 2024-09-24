'''
Rabin-Karp fingerprint search


note:
Theory. 
    If Q is a sufficiently large random prime (about MN^2),
    then the probability of a false collision is about 1/N.

Practice. 
    Choose Q to be a large prime (but not so large to cause overflow).
    Under reasonable assumptions, probability of a collision is about 1/Q.
'''

from sympy import randprime

class RK:
    def __init__(self, pat) -> None:
        self.pat = pat
        self.M = len(self.pat)
        
        self.R = 10 # base
        self.Q = randprime(10**100, 10**101) # 生成一个范围内的随机素数
        self.RM = self.R**(self.M-1) % self.Q
        self.patHash = self._hash(self.pat, self.M)
    
    # Compute hash for M-digit key
    def _hash(self, key, m):
        h=0
        for i in range(m):
            h = (self.R*h + ord(key[i])) % (self.Q)
        return h

    def search(self, txt:str):
        N = len(txt)
        txtHash = self._hash(txt, self.M)
        if self.patHash== txtHash:
            return 0
        
        for i in range(self.M, N):
            txtHash = (txtHash - self.RM*ord(txt[i-self.M])) % self.Q
            txtHash = (txtHash*self.R + ord(txt[i])) % self.Q
            
            # log
            # print(i, self.pat, self.patHash, txt[i-self.M+1: i+1], txtHash)
            if self.patHash == txtHash:
                return i-self.M+1 # hash code match, find pat
        
        return N # not find
    