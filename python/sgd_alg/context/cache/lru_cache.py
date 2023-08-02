# todo 应为是lib库实现，
#  双向链表和ndoe的逻辑需要统一规划一下，
#  不需要每个文件里都重新定义一遍，需要复用。

class Node:
    def __init__(self, k, v, p_pre, p_next=None):
        self.key = k
        self.val = v
        self.next = p_next
        self.pre = p_pre


class LRUCache:
    """
    设计思路
    用双向链表去存储具体数据的节点
    get,put 用 基于hash的dict来达到O(1)的操作
    """

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.index = dict()  # hash table
        self.tail = self.head = Node(k=0, v=0, p_pre=None)  # 初始占位节点

    def get(self, key: int) -> int:
        if key not in self.index:
            return -1
        else:
            cur_node = self.index[key]
            # 重置操作时间
            self.move_node_to_tail(cur_node)
            return cur_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.index:
            # key存在，直接更新value
            cur_node = self.index[key]
            cur_node.val = value
            # 重置操作时间
            self.move_node_to_tail(cur_node)
        else:  # key不存，alloc new node for current unseen kv pair
            new_node = Node(key, value, p_pre=self.tail)
            # 整理tail前后指针
            self.tail.next = new_node
            self.tail = new_node
            # 建立该值的索引，以便 O(1) 查询
            self.index[key] = new_node
            # update size
            self.size_self_increase()

    def move_node_to_tail(self, cur_node):
        # 移动cur_node到队列末尾，表示操作时间上的先后关系
        if self.tail != cur_node:
            # 记录下断裂处前后的node
            pre_node = cur_node.pre
            next_node = cur_node.next
            # 拼接断裂处
            pre_node.next = next_node
            next_node.pre = pre_node
            # 在队列末尾双向拼接cur_node
            self.tail.next = cur_node
            cur_node.pre = self.tail
            # 重置尾指针
            self.tail = cur_node
            self.tail.next = None
        # 双向链表的设计保证上述操作复杂度O(1)

    def size_self_increase(self):
        self.size += 1
        if self.size > self.capacity:
            self.vicitm()
            assert self.size == self.capacity

    # 如果当前size > capacity 需要驱逐旧node
    def vicitm(self):
        # 调用此驱逐node函数时，必然有capacity+1个节点，所以不用考虑特殊情况
        old_node = self.head.next
        new_old_node = old_node.next
        # 整理head前后指针
        self.head.next = new_old_node
        new_old_node.pre = self.head
        # 从index里删除old node
        del self.index[old_node.key]
        # 驱逐成功，size-1
        self.size -= 1

    # 链表和索引状态日志（查bug时使用）
    def inner_state_log(self):
        print("size:", self.size)
        print("capacity:", self.capacity)
        print("index:", self.index)

        p = self.head
        print("link-list:[", end="")
        while p.next:
            p = p.next
            print((p.key, p.val), end="-")
        print(']')

