Symbol table
-
- 朴素的实现，直接unorder array 线性查找、插入、删除
- 二分查找实现（双order array实现）， 插入删除仍为线性，search（检索） logN

- 二分查找树
  - 思路：基于order array的二分查找方式，插入与删除操作需要整个移动 part of array items
      这个复杂度代价过高，采用树型结构，利用链表的可操作性，降低复杂度

由于二分查找树的不平衡问题，计算代价和树的高度成正比，所以需要发展平衡二叉树算法。

平衡二叉树算法
-
- 2-3树
  - dsf

- 红黑树
  - xx
- B+树
  - sadg

另一种思路Hash
-
-

相关应用
-
