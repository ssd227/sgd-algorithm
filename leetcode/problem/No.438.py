# 438. 找到字符串中所有字母异位词 https://leetcode.cn/problems/find-all-anagrams-in-a-string/

def dict_is_same(dic, tar_dic):
    
    for k, v in dic.items():
        if k in tar_dic:
            if v != tar_dic[k]:
                return False
        else:
            return False
    return True

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        N = len(p)

        target = {}
        for c in p:
            if c not in target:
                target[c] = 1
            else:
                target[c]+=1

        cur_count = dict()
        resid = []
        
        i = 0
        while i < len(s)-N+1:
            # 先统计目前window-N内的所有字符
            cur_count = dict()
            window_count_done = True

            for j in range(N):
                c = s[i+j]
                if s[i+j] not in target:
                    i = i+j+1 # 大跨步
                    window_count_done = False
                    break
                
                if c in cur_count:
                    cur_count[c] += 1
                else:
                    cur_count[c] = 1

            # if i == 6:
            #     print(window_count_done, cur_count)

            if window_count_done:
                # 窗口数据统计完毕
                is_same = dict_is_same(cur_count, target)
                if is_same:
                    resid.append(i)

                    # 正确的字串，再便利的移动几步
                    while i+N < len(s)  and s[i+N] == s[i]:
                        i+=1
                        resid.append(i)
                i+=1

            else:
                continue

        return resid