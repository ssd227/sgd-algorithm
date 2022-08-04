import random
import time

from sgd_alg.data_struct.heap import PriorityHeap


def ex_priority_heap():
    heap = PriorityHeap()
    for i in [9, 5, 4, 3, 2, -9]:
        heap.insert(i)

    heap.log()
    heap.pop_head()
    heap.log()
    heap.pop_head()
    heap.log()

    for i in range(7):
        heap.pop_head()
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
    # ex_priority_heap()
    ex_press_test()
