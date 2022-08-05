"""
Note. Array size M must be greater than number of key-value pairs N.

hash ST（linear prob）
    Typical choice: M ~ 2 * N
    # probes for search hit is about 3/2
    # probes for search miss is about 5/2

M: hash桶的个数
N: 总数据量


todo
    Q. How to delete?
    Q. How to resize?

"""


class LinearProbingHashST:
    def __init__(self, b_num):
        self.bucket_num = b_num
        self.buckets = [None] * b_num

    def hash(self, key):
        return hash(key) % self.bucket_num

    def put(self, key, value) -> bool:
        idx = self.hash(key)

        for i in range(self.bucket_num):
            b_idx = (idx + i) % self.bucket_num
            if self.buckets[b_idx] is None:
                self.buckets[b_idx] = (key, value)
                return True

        print('hash symbol table is full, put failed!!')
        return False

    def get(self, key):
        idx = self.hash(key)

        for i in range(self.bucket_num):
            b_idx = (idx + i) % self.bucket_num
            if self.buckets[b_idx] is not None:
                if self.buckets[b_idx][0] == key:
                    return self.buckets[b_idx][1]
            else:
                break
        return None

    def log_inner_state(self):
        print(self.buckets)


if __name__ == '__main__':
    n = 3
    m = 2 * n  # 最优两倍的数据量
    # 由于不可能插满，所以溢出问题不存在。 必定有slot 可以插满
    # todo 但是就不能使用 lazy delete， 用(key，null)表示不存在
    hst = LinearProbingHashST(m)

    for i in range(n):
        hst.put(i, i)

    hst.log_inner_state()

    print(hst.get(1))
    print(hst.get(2))
    print(hst.get(3))
