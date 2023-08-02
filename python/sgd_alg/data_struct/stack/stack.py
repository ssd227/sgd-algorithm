"""
stack.py module

实现类
    StackInterface 栈的抽象类
    LinkListStack 单向链表
    ArrayStack  定长数组
    ResizingArrayStack 可变长数组

tips：
    LinkListStack 操作单链表需要额外的时间和空间，操作都是常数时间
    ResizingArrayStack 浪费额外的数据存储空间，重新分配空间时操作为O(N)时间, 平均为常数时间。

todo 压力测试两种类的极限情况（内存和时间上的优略）
"""


class StackInterface:
    def __init__(self):
        pass

    def push(self, item):
        raise NotImplementedError("Should have implemented this")

    def pop(self):
        raise NotImplementedError("Should have implemented this")

    def is_empty(self) -> bool:
        raise NotImplementedError("Should have implemented this")

    def size(self):
        raise NotImplementedError("Should have implemented this")


class Node:
    def __init__(self, v, p_next=None):
        self.val = v
        self.next = p_next


class LinkListStack(StackInterface):
    """
    用单向链表管理数据，push pop 操作的代价都是O(1)
    实现上也不复杂，暂时没看出来有啥弊端
    """

    def __init__(self):
        super().__init__()
        self.head = None
        self.size_ = 0

    def push(self, item):
        # insert a new node at front of linked list
        self.head = Node(item, self.head)
        self.size_ += 1

    def pop(self):
        if not self.is_empty():
            res_item = self.head.val
            self.head = self.head.next
            self.size_ -= 1
            return res_item
        return None

    def is_empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_


class ArrayStack(StackInterface):
    """
    定长数组管理数据
    """

    def __init__(self, capacity):
        super().__init__()

        self.array = [None] * capacity
        self.capacity = capacity
        # size_ 在这里可以当作数组下标
        self.size_ = 0

    def push(self, item):
        if self.size_ < self.capacity:
            self.array[self.size_] = item
            self.size_ += 1
        else:
            print("stack is full, insert {} failed!", item)

    def pop(self):
        if not self.is_empty():
            res_item = self.array[self.size_-1]
            self.size_ -= 1
            return res_item
        print("stack is empty, no elem to pop!")
        return None

    def is_empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_


class ResizingArrayStack(StackInterface):
    """
    变常数组管理数据
    """

    def __init__(self):
        super().__init__()
        self.low_capacity = 2
        self.capacity = self.low_capacity
        self.array = [None] * self.capacity
        # size_ 在这里可以当作数组下标
        self.size_ = 0

    def push(self, item):
        # assert there is slot for new data to push
        self.resizing_capacity()
        self.array[self.size_] = item
        self.size_ += 1

    def pop(self):
        if not self.is_empty():
            res_item = self.array[self.size_-1]
            self.size_ -= 1
            self.resizing_capacity()
            return res_item
        print("stack is empty, no elem to pop!")
        return None

    def resizing_capacity(self):
        # print(self.size_, self.capacity)
        # current array is full, double array size
        if self.size_ >= self.capacity:
            self.array += [None] * self.capacity
            self.capacity *= 2
        # current array is two large
        # halve size of array when array is one-quarter full
        elif self.size_ <= (self.capacity // 4):
            self.capacity = max(self.low_capacity, self.capacity // 2)
            self.array = self.array[:self.capacity]

    def is_empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_


