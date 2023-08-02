"""
优先队列 priority heap

使用场景：
    Find the largest M items in a stream of N items.
    N非常大，M范围限制在内存可接受范围

主要操作：
1、插入 将元素插入array树的末端，进行switch_up
2、switch_down 当parent node val 大于child node val
    选取较大的node进行父子交换（可以以较少的下沉操作找到合理的位置）。
3、删除 pop堆顶元素，将树末端元素插入root，执行switch_down操作

下表从1开始，可以简化找parent 和 child 的取模运算


时间复杂度：NlogN
空间复杂度： N+1


todo 应用（粒子碰撞模拟） 可以写写看基于事件的粒子运动模拟
Time-driven simulation. N bouncing balls in the unit square.

Main loop.
    Delete the impending event from PQ (min priority = t).
    If the event has been invalidated, ignore it.
    Advance all particles to time t, on a straight-line trajectory.
    Update the velocities of the colliding particle(s).
    Predict future particle-wall and particle-particle collisions involving the
    colliding particle(s) and insert events onto PQ.

感觉复杂度还是好高，需要预测所有碰撞加入heap中，然后选出min timet更新
状态因碰撞改变了的粒子，与之相关的所有事件重新计算dt，然后改变在小根堆里的位置


todo 插入一直可以无条件进行，查满了就需继续插，然后推出一个队列末尾的数

"""

class PriorityHeap:
    def __init__(self, capacity, compare_f):
        self.order = compare_f
        
        self.capacity = capacity
        self.size = 0
        
        self.arr = [0]*self.capacity # 使用List来表示树结构
    
    def add(self, x):
        if self.size < self.capacity:
            self.arr[self.size] = x
            self.size += 1

            self.up(self.size-1) # 新加元素，交换到正确的位置
            
            return True
        
        # print("add item failed! heap is full, remove item first")
        return False
    
    def auto_add(self, x):
        # 当堆占满后，自动pop 堆顶元素，然后添加新的item
        ok = self.add(x)
        
        if (not ok) and (not self.order(x, self.arr[0])): # 堆占满了， 且x比堆顶元素强点，
            self.remove() # 删掉最弱的堆顶元素，插入x
            assert self.size == (self.capacity-1)
            self.add(x)

    def pop():
        # 依次取出堆中最小的元素
        pass
    
    def all_item(self):
        return self.arr[:self.size]
    
    def top(self):
        # 返回堆顶元素
        return self.arr[0]
    
    def remove(self):
        # 删除堆顶元素，把最后一位补上，并下沉到正确的位置
        self.size-=1
        self.arr[0] = self.arr[self.size]
        
        i = 0
        # parent keep order of left and right children

        # print("down-log", self._keep_order(i, self.left(i)), self._keep_order(i, self.right(i)))
        while not (self._keep_order(i, self.left(i))
                   and self._keep_order(i, self.right(i))):
            
            lid, rid = self.left(i), self.right(i)
            nextid = lid  if self._keep_order(lid, rid) else rid # 选择更不合理的一个子节点交换
            # print("down-swap", i, nextid)

            if nextid:
                self._swap(i, nextid)
                i = nextid
    
    # help func - 使用id来比较arr值
    def _keep_order(self, i, j):
        if j is None:
            return True
        return self.order(self.arr[i], self.arr[j])
    
    # help func - 使用id来交换arr值
    def _swap(self, i,j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            
    def up(self, i):
        # 最后一位元素向上交换，上浮动至正确的位置
        while (not self._keep_order(self.parent(i), i)) and (self.parent(i) != i):
            self._swap(self.parent(i), i)
            # print("up-swap", self.parent(i) , i)
            i = self.parent(i)
    
    def parent(self, i):
        if i > 0:
            return (i-1)//2
        if i == 0:
            return 0
    
    def left(self, i):
        # 超过size需返回None
        lid = 2*i +1
        return lid if lid < self.size else None
    
    def right(self, i):
        # 超过size需返回None
        rid = 2*(i+1)
        return rid if rid < self.size else None


# tips 使用compare函数，导致比较函数调用的开销直线增大10%

# compare function
def larger(a, b):
    return a > b

def smaller(a, b):
    return a < b

def maxheap(capacity):
    return PriorityHeap(capacity, compare_f=larger)

def minheap(capacity):
    return PriorityHeap(capacity, compare_f=smaller)


# 实现的另一个版本
class PriorityHeapOldVersion:
    def __init__(self, capacity, compare_f):
        self.tree = [0] * (capacity+1)
        self.capacity = capacity
        self.size = 0

        self.compare_f = compare_f

    def insert(self, x):
        if self.size >= self.capacity:
            print("exceed max capacity, insert fail!!!")
            return
        self.tree[self.size] = x
        self.switch_up(self.size)
        self.size += 1

    def get_head(self):
        if self.size > 0:
            return self.tree[0]

    def pop_head(self):
        if self.size == 0:
            return None
        head = self.get_head()
        self.tree[0] = self.tree[self.size - 1]
        self.size -= 1
        self.switch_down(0)
        return head

    def switch_val(self, x1, x2):
        self.tree[x1], self.tree[x2] = self.tree[x2], self.tree[x1]

    def switch_up(self, idx):
        while idx != 0:
            fa_id = (idx - 1) // 2
            if self.compare_f(self.tree[idx], self.tree[fa_id]):
                self.switch_val(fa_id, idx)
                idx = fa_id
            else:
                break

    def switch_down(self, idx):
        while (2 * idx + 1) < self.size:
            le = idx * 2 + 1
            ri = le + 1

            child_chosen = None
            if ri >= self.size:
                child_chosen = le
            else:
                child_chosen = le if self.compare_f(self.tree[le], self.tree[ri]) else ri

            # switch with child chosen
            if self.compare_f(self.tree[child_chosen], self.tree[idx]):
                self.switch_val(child_chosen, idx)
                idx = child_chosen
            else:
                break

    # helper functions below
    def size(self):
        return self.size()

    def is_full(self) -> bool:
        return self.size >= self.capacity

    def is_empty(self) -> bool:
        return self.size <= 0

    def log(self):
        ss = ""
        for i in range(self.size):
            ss += str(self.tree[i]) + ', '
        print('test: ', ss)
