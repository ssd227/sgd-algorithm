import random
import time

from sgd_alg.data_struct.heap import PriorityHeap


"""
使用小根堆，keep max 4。还是可以实现数据流的大筛选
需要手动控制一下pop head的时机
todo 整合成完整可调用的库
"""
def ex_priority_heap():
    heap = PriorityHeap(capacity=4, reverse=True)
    for i in [1, 2, 3, 4, 5, -1, -2]:
        if heap.is_full():
            if heap.get_head() < i:
                heap.pop_head()
        heap.insert(i)
        heap.log()
    heap.log()


def ex_press_test():
    # op-size：1e6 cost time: 3.461273431777954
    heap = PriorityHeap()
    t1 = time.time()
    for _ in range(int(1e6)):
        # print(heap.size)
        if random.random() > 0.3:
            if heap.is_full():
                for i in range(40):
                    heap.pop_head()
            heap.insert(random.random())
        else:
            heap.pop_head()

    print('cost time:', time.time() - t1)


if __name__ == '__main__':
    ex_priority_heap()
    # ex_press_test()
