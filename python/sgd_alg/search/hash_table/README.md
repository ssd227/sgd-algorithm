hash 函数

Combine each significant field using the 31x + y rule

Basic rule. Need to use the whole key to compute hash code;
consult an expert for state-of-the-art hash codes.


### Hash code. 
    An int between -231 and 231 - 1.
### Hash function. 
    An int between 0 and M - 1 (for use as array index).


注意： 哈希函数 由于seed的不动，导致在不同运行时中无法保证hash值一致。

todo
Q. How to delete?
Q. How to resize?

todo hash 最坏的查找，插入，删除为什么也是logN呢
hash-st average 3-5下操作就能完成各种操作


### hash（链表）
    Typical choice: M ~ N / 5 ⇒ constant-time ops.
    M: hash桶的个数
    N: 总数据量


### hash（linear prob）
    Typical choice: M ~ 2 * N
    # probes for search hit is about 3/2
    # probes for search miss is about 5/2