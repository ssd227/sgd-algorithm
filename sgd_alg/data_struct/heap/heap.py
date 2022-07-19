class Heap:
    def __init__(self, capacity=100):
        self.tree = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def append(self, x):
        if self.size >= self.capacity:
            print("exceed max capacity")
            return

        self.tree[self.size] = x
        self.small_to_top(self.size)
        self.size += 1

    def switch_val(self, x1, x2):
        self.tree[x1], self.tree[x2] = self.tree[x2], self.tree[x1]

    def small_to_top(self, idx):
        while idx != 0:
            fa_id = (idx - 1) // 2
            if self.tree[idx] < self.tree[fa_id]:
                self.switch_val(fa_id, idx)
                idx = fa_id
            else:
                break

    def get_head(self):
        if self.size > 0:
            return self.tree[0]

    def pop_head(self):
        if self.size == 0:
            return None
        head = self.get_head()
        self.tree[0] = self.tree[self.size-1]
        self.size -= 1
        self.large_to_down(0)
        return head

    def large_to_down(self, idx):
        while idx < self.size:
            le = idx * 2 + 1
            ri = le + 1


            # print(idx)
            # print(self.tree)

            # no child node
            if le >= self.size and ri >= self.size:
                break

            elif le < self.size and ri >= self.size:
                if self.tree[idx] > self.tree[le]:
                    self.switch_val(idx, le)
                    idx = le  # update
                else:
                    break
            else:  # two child node, switch smaller one
                sw_idx = None
                if self.tree[le] < self.tree[ri]:
                    sw_idx = le
                else:
                    sw_idx = ri

                if self.tree[sw_idx] < self.tree[idx]:
                    self.switch_val(sw_idx, idx)
                    idx = sw_idx  # update
                else:
                    break

    def log(self):
        ss = ""
        for i in range(self.size):
            ss += str(self.tree[i])+', '
        print('test: ', ss)

def test():
    heap = Heap()
    for i in [9, 5, 4, 3, 2, -9]:
        heap.append(i)

    heap.log()

    heap.pop_head()
    heap.log()
    heap.pop_head()
    heap.log()

    for i in range(7):
        heap.pop_head()
        heap.log()

if __name__ == '__main__':
    test()
