# 目前先实现个简单的, 测试一下python 迭代器的使用方式
# todo 操作in优化成O1复杂度 (也就是set 的 in 操作是怎么做到O1的)


class Bag:
    def __init__(self):
        self.array_ = []

    def add(self, x):
        self.array_.append(x)

    def item_in(self, x):
        return x in self.array_  # 目前是个ON操作

    def size(self):
        return len(self.array_)

    def __len__(self):
        return len(self.array_)

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < self.size():
            x = self.array_[self.idx]
            self.idx += 1
            return x
        else:
            raise StopIteration

