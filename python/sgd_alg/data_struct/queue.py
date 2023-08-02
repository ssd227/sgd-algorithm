"""
queue.py module

实现类
    LinkListQueue 链表队列
    ResizingArrayQueue 可变数组队列

todo 目前来看代码对是对的，但是可变长度的array，还附带带mod循环处理的就非常的复杂。极其容易出错
todo 测试代码要好好写一写了 ResizingArrayQueue， 写个随机进队列、出队列的操作，assert 满足先进先出的规则
todo Resizeing array queue是真难写，但是好像可以用两个stack 模拟queue（这两种方式的极限性能有没有差距）
"""


class QueueInterface:
    def __init__(self):
        pass

    def enqueue(self, item):
        raise NotImplementedError("Should have implemented this")

    def dequeue(self):
        raise NotImplementedError("Should have implemented this")

    def is_empty(self) -> bool:
        raise NotImplementedError("Should have implemented this")

    def size(self):
        raise NotImplementedError("Should have implemented this")


class Node:
    def __init__(self, v, p_next=None):
        self.val = v
        self.next = p_next


class LinkListQueue(QueueInterface):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size_ = 0

    def enqueue(self, item):
        cur_node = Node(item)
        if self.size() == 0:
            self.head = self.tail = cur_node
        else:
            self.tail.next = cur_node
            self.tail = cur_node
        self.size_ += 1

    def dequeue(self):
        if not self.is_empty():
            head_node = self.head
            self.head = self.head.next
            self.size_ -= 1
            if self.size() == 0:
                self.tail = None
            return head_node.val

        print('queue is empty! no elem to dequeue! return None')
        return None

    def is_empty(self) -> bool:
        return self.size_ == 0

    def size(self):
        return self.size_


class ResizingArrayQueue(QueueInterface):
    def __init__(self):
        super().__init__()

        self.low_capacity = 2
        self.capacity = self.low_capacity
        self.array = [None] * self.capacity

        self.size_ = 0
        self.head_id = 0
        self.tail_id = 0

    def enqueue(self, item):
        self.resizing_capacity()
        self.array[self.tail_id] = item
        self.size_ += 1
        if self.size() == 1:
            self.head_id = self.tail_id
        self.tail_id = (self.tail_id + 1) % self.capacity

    def dequeue(self):
        self.resizing_capacity()

        if not self.is_empty():
            res_item = self.array[self.head_id]
            self.head_id += 1
            self.size_ -= 1
            self.resizing_capacity()
            return res_item
        print('queue is empty! no elem to dequeue! return None')
        return None

    # 有循环填充问题，容易出错
    def resizing_capacity(self):
        # print(self.size(), self.capacity, self.head_id, self.tail_id)
        # current array is full, double array size
        if self.size() >= self.capacity:
            old_capacity = self.capacity
            old_array = self.array
            old_size = self.size()
            self.capacity *= 2  # 不同点
            self.array = [None] * self.capacity
            for i in range(old_size):
                self.array[i] = old_array[(self.head_id + i) % old_capacity]
            self.head_id = 0
            self.tail_id = old_size

        # current array is two large
        # halve size of array when array is one-quarter full
        elif self.size() <= (self.capacity // 4):
            old_capacity = self.capacity
            old_array = self.array
            old_size = self.size()
            self.capacity = max(self.low_capacity, self.capacity // 2)  # 不同点
            self.array = [None] * self.capacity
            for i in range(old_size):
                self.array[i] = old_array[(self.head_id + i) % old_capacity]
            self.head_id = 0
            self.tail_id = old_size

    def is_empty(self) -> bool:
        return self.size_ == 0

    def size(self):
        return self.size_
