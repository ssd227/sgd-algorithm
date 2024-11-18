'''
skip list 跳跃表
Generalization of sorted linked lists, so simple to implement


max_level_num = n
合理list长度不应超过2**n，否则性能向普通链表逐渐退化

备注：
    * 跳跃表实际处理起来也没说的那么容易
        * 半天是需要的
        * 感觉比红黑树实现可难多了
    * 写完后的代码也不是很好阅读
    
    指针较多，更新起来还挺绕。数据结构的随机性还不太好测试。

delete bug分析
    参见 app/search/skip_list_bug.log

todo
    头尾节点最好都用哨兵node表示，简化None指针的处理情况。 目前的代码迭代逻辑比较混乱
'''

import numpy as np

__all__ = ['SkipList', 'SkipListNode', 'LevelItem', 'RandomManager']

global_node_uid = -1


class RandomManager():
    '''
        功能：
        * 1/2概率增加level的高度
        * cache缓存批量生成的随机数，提高调用效率  
    '''

    def __init__(self) -> None:
        self.cache = []

    def get_random_height(self, max_level_num):
        level = 1
        while level < max_level_num:
            if len(self.cache) <= 0:
                self.cache += np.random.uniform(0, 1, 500).tolist()  # 补充随机数
            # 每次投掷硬币决定
            p = self.cache.pop(0)
            if p > 0.5:
                level += 1
            else:
                break

        assert level <= max_level_num, '{} <= {}'.format(level, max_level_num)
        return level


class LevelItem():
    def __init__(self, next=None, span=0) -> None:
        self.next = next  # 前进指针
        self.span = span  # 跨度，用于rank计算

    def log(self):
        return '(next:{}, span:{})'.format(self.next.uid if self.next else "None",
                                           self.span).ljust(20)


class SkipListNode:
    def __init__(self, level_num, key=None, value=None) -> None:
        assert level_num > 0, "Assert level_num > 0"
        self.level = [LevelItem() for _ in range(level_num)]  # list(LevelItem)
        self.backward = None  # 后退指针

        self.key = key
        self.value = value

        self.tmp_rank = 0

        self.uid = self.get_uid()
        global global_var  # 声明使用全局变量

    def get_uid(self):
        global global_node_uid
        global_node_uid += 1
        return global_node_uid

    def log(self):
        level_log = ' '.join([item.log() for item in self.level])
        return 'Node id:{}, level:[{}], bw:{}, key:{}, value:{}, tmp_rank:{}'.format(
            self.uid,
            level_log,
            self.backward.uid if self.backward else "None",
            self.key,
            self.value,
            self.tmp_rank)

    def log_value(self):
        level_log = ' '.join([item.log() for item in self.level])
        return (self.uid,
                level_log,
                self.backward.uid if self.backward else "None",
                self.key,
                self.value,
                self.tmp_rank)


class SkipList:
    def __init__(self, max_level_num=32) -> None:
        # reset Node id for testing
        global global_node_uid
        global_node_uid = -1

        self.max_level_num = max_level_num

        self.header = SkipListNode(max_level_num)  # 初始固定head Node
        self.tail = None  # 尾节点
        self.level = 1
        self.length = 0  # skip list 存储的kv对个数
        self.rand_mgr = RandomManager()

    # 按照表格化输出skip list
    def log(self):
        data = []
        data.append(['uid', 'level info:', 'bw', 'Key', 'Value', 'tmp_ank'])  # 表头
        # 按照level 1 遍历收集所有节点数据
        p = self.header
        while p:
            data.append(p.log_value())
            p = p.level[0].next

        for row in data:
            print(
                f"{str(row[0]).ljust(8)}{str(row[3]).ljust(8)}{str(row[4]).ljust(8)}{str(row[2]).ljust(7)}{str(row[1]).ljust(15)}")
        print('-------' * 20)

    def get(self, key):
        i = self.level - 1  # 从最高level开始遍历
        p = self.header

        while p.level[i].next or i >= 0:
            if i == -1:
                return None  # 搜索失败

            # print(f'[Log][get:{key}] @Node id:{p.uid}, level:{i}')
            if p.level[i].next:
                # print(f'\t[log][get-inner:{key}] next key:{p.level[i].next.key}', key == p.level[i].next.key)
                if key == p.level[i].next.key:
                    return p.level[i].next.value  # 查询成功
                elif key > p.level[i].next.key:
                    p = p.level[i].next
                else:
                    i -= 1  # 降低level，缩小搜索空间[p.key, p.next.key]

            else:  # key < inf (空指针的情况)  / p.level[i].next is None
                i -= 1

        return None

    def put(self, key, value) -> None:
        i = self.level - 1  # 从最高level开始遍历
        p = self.header

        cur_rank = 0  # 头节点设为0
        p.tmp_rank = cur_rank

        ### find插入位置
        pre_map = {}  # 找到插入位置时的所有前置节点 {level的高度 : 前置节点}
        while p.level[i].next or i >= 0:
            if i == -1:
                break
            # print(f'[Log][put:{key}] @Node id:{p.uid}, level:{i}')
            if p.level[i].next:
                # print(f'\t[log][put-inner:{key}] next key:{p.level[i].next.key}', key == p.level[i].next.key)
                if key == p.level[i].next.key:
                    p.level[i].next.value = value
                    return  # 不需要修改list元信息

                elif key > p.level[i].next.key:
                    cur_rank += p.level[i].span
                    p = p.level[i].next  # move p
                    p.tmp_rank = cur_rank  # update rank
                    pre_map[i] = p  # 同级前置节点更新

                else:  # key < p.level[i].next.key
                    pre_map[i] = p  # 往下走，记录前置节点（同层会被后者取代）
                    i -= 1  # 降低level，缩小搜索空间[p.key, p.next.key]

            else:  # key < inf (空指针的情况)  / p.level[i].next is None
                pre_map[i] = p
                i -= 1
        assert len(pre_map) > 0, "assert len(pre_map) > 0"

        ### 新增节点
        cur_rank += 1
        level_num = self.rand_mgr.get_random_height(self.max_level_num)  # 随机高度，0.5概率增高1
        new_node = SkipListNode(level_num=level_num,
                                key=key,
                                value=value)

        if p is None:  # 指向list末尾
            self.tail = new_node  # 更新tail

        # 前置节点集合（pre_map）链表指针操作
        for j in range(level_num):  # 0,1,2,...,level_num-1
            if j < self.level:
                pj = pre_map[j]  # 找到level_j的前置节点pj

                # update span
                old_span = pj.level[j].span
                pj.level[j].span = cur_rank - pj.tmp_rank

                if old_span == 0:  # insert tail
                    new_node.level[j].span = 0
                    # print(f'[log尾巴] level:{j}, pj.rank:{pj.tmp_rank}, old_span:{old_span}, cur_rank:{cur_rank},')
                else:  # insert middle
                    new_node.level[j].span = pj.tmp_rank + old_span + 1 - cur_rank
                    # print(f'[log中间] level:{j}, pj.rank:{pj.tmp_rank}, old_span:{old_span}, cur_rank:{cur_rank},')

                # update list struct
                new_node.level[j].next = pj.level[j].next
                pj.level[j].next = new_node

                # backward的处理
                if j == 0:
                    new_node.backward = pj  # p.bw -> 前一个节点
                    if new_node.level[0].next:
                        new_node.level[0].next.backward = new_node  # 后一个节点的bw 指向本节点

            else:  # 大level id值，直接用head Node直连
                self.header.level[j].span = cur_rank
                self.header.level[j].next = new_node

        # span 另一种需要补全的case
        if level_num < self.level:
            for i in range(level_num, self.level):
                node = pre_map[i]
                old_span = node.level[i].span
                if old_span > 0:
                    pre_map[i].level[i].span += 1

        # 修改list元信息
        self.length += 1
        self.level = max(self.level, level_num)

    def delete(self, key):
        i = self.level - 1
        p = self.header

        ### find插入位置
        pre_map = {}  # 找到插入位置时的所有前置节点 {level的高度 : 前置节点}
        find = False
        while p.level[i].next or i >= 0:
            if i == -1:
                break
            # print(f'[Log][delete:{key}] @Node id:{p.uid}, level:{i}')
            if p.level[i].next:
                # print(f'\t[log][delete-inner:{key}] next key:{p.level[i].next.key}', key == p.level[i].next.key)
                if key == p.level[i].next.key:
                    find = True
                    pre_map[i] = p
                    i -= 1

                elif key > p.level[i].next.key:
                    p = p.level[i].next  # move p
                    pre_map[i] = p  # 同级前置节点更新

                else:  # key < p.level[i].next.key
                    pre_map[i] = p  # 往下走，记录前置节点（同层会被后者取代）
                    i -= 1  # 降低level，缩小搜索空间[p.key, p.next.key]

            else:  # key < inf (空指针的情况)  / p.level[i].next is None
                pre_map[i] = p
                i -= 1
        assert len(pre_map) > 0, "assert len(pre_map) > 0"

        if not find:
            return  # 未找到key，不删除
        p = p.level[0].next  # p 指向当前待删除Node

        ## 从链表中删除目标节点，更新span、backward、链表结构
        # backward的处理
        if p.level[0].next:
            p.level[0].next.backward = p.backward
        else:  # 删除尾节点
            self.tail = p.backward

        level_num = len(p.level)  # 待删除节点高度
        for i, pi in pre_map.items():
            # print('delete level:{}, pi:{}, p:{}.'.format(i, pi.key, p.key))

            # 按 当前节点p的level高度 分两种情况
            if i < level_num:
                # 修正span & 链表
                pi.level[i].next = p.level[i].next
                pi.level[i].span += p.level[i].span - 1

                if pi.level[i].next is None:
                    pi.level[i].span = 0

            else:
                # 修正span
                if pi.level[i].span > 0:
                    pi.level[i].span -= 1

        # 修改list元信息
        self.length -= 1
        # self.level = max(self.level, level_num) # todo 不好处理，但是不处理也不影响正确性

    # 按照get流程走一遍，累加span
    def rank(self, key):
        i = self.level - 1
        p = self.header
        cur_rank = 0

        while p.level[i].next or i >=0:
            if p.level[i].next:
                if key == p.level[i].next.key:
                    return cur_rank + p.level[i].span  # 查询成功

                elif key > p.level[i].next.key:
                    cur_rank += p.level[i].span
                    p = p.level[i].next

                else:
                    i -= 1  # 降低level，缩小搜索空间[p.key, p.next.key]
                    if i == -1:  # 搜索失败
                        return -1
            else:  # key < inf (空指针的情况)  / p.level[i].next is None
                i -= 1
                if i == -1:
                    return -1
        return -1

    def size(self):
        return self.length
