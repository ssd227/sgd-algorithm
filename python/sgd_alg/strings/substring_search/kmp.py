'''
Knuth-Morris-Pratt substring search

Note:
    * R是字符集合
        实现时只考虑pat中的字符
        未出现的字符在search时忽略，状态转移到0(未匹配到任何字符)

    * dfa的数据结构
        * choice 1 使用字典，value恒定大小数组
        * choice 2 使用数组，建立字符和id的映射关系
            效率可能高点，缓存命中高，好整体复制一列
            
    * todo 处理string重叠部分匹配结果
        例： pat-ABA, txt-ABABABA
        需要扩展dfa在 len(pat)位置上的值，补充一列
        或者直接定义
'''

class KMP:
    def __init__(self, pat) -> None:
        self.pat = pat
        self.alphas = set(self.pat)
        self.a2i = {k:v for k, v in zip( self.alphas, range(len(self.alphas)))}
        
        # DFA [state_i][alpha_c], 在状态i，接受char_x后转移到的新state_next
        self.dfa = self._build_dfa()

    def _build_dfa(self):
        # m 定义为 accept state
        m, n = len(self.pat), len(self.alphas) # DFA [state_i][alhpa_c]
        dfa = [[0]*n for _ in range(m)] # init dfa

        dfa[0][self.a2i[self.pat[0]]] = 1
        
        X = 0
        for state_i in range(1, m): # 遍历pat的所有状态
            # copy mismatch cases
            dfa[state_i] =  dfa[X][:]
            
            # set match case
            dfa[state_i][self.a2i[self.pat[state_i]]] = state_i+1
            
            # update restart state
            X = dfa[X][self.a2i[self.pat[state_i]]]
        
        return dfa

    def search(self, txt:str):
        i = state_j = 0
        while i<len(txt) and state_j<len(self.pat):
            # 处理未出现的字符
            cc = txt[i]
            if cc not in self.a2i:
                state_j = 0
            else:
                a_id = self.a2i[cc] # 当前文本匹配字符txt[si]的alpha id
                state_j = self.dfa[state_j][a_id] 
            i+=1
        if state_j==len(self.pat):
            return i-len(self.pat)
        else:
            return len(txt) # 未匹配返回文本最后一位 i+1
    