"""
Separate chaining symbol table
hash ST(链表)

    Typical choice: M ~ N / 5 ⇒ constant-time ops.
    M: hash桶的个数
    N: 总数据量

todo
    Q. How to delete?
    Q. How to resize?

"""
import random
import xxhash


class Node:
    def __init__(self, k=0, v=0, nxt=None):
        self.key = k
        self.val = v
        self.next = nxt


class SeparateChainingHashST:
    def __init__(self, b_num):
        self.bucket_num = b_num
        self.buckets = [None] * b_num

    def hash(self, key):
        # todo xxhash 函数只处理a bytes-like object is required, not 'int'
        # hash_code = xxhash.xxh64_intdigest(bytes(key), seed=20141025)

        # 暂时先用python自带的hash code
        return hash(key) % self.bucket_num

    def get(self, key):
        b_idx = self.hash(key)
        slot_node = self.buckets[b_idx]
        while slot_node:
            if slot_node.key == key:
                return slot_node.val
            slot_node = slot_node.next
        return None

    def put(self, key, value):
        b_idx = self.hash(key)
        slot_node = self.buckets[b_idx]

        if slot_node is None:
            self.buckets[b_idx] = Node(key, value)

        while slot_node:
            if slot_node.key == key:
                slot_node.val = value
                break
            elif slot_node.next is None:
                slot_node.next = Node(key, value)
                break
            else:
                slot_node = slot_node.next

    def log_inner_state(self):
        for i in range(self.bucket_num):
            sa = []
            cur_node = self.buckets[i]
            while cur_node:
                sa.append((cur_node.key, cur_node.val))
                cur_node = cur_node.next
            print('slot {}:{}'.format(i, sa))