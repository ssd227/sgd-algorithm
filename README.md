# sgd_algorithm（python-version）

## 简介
以《algorithm 4th》为基本框架，整合常用的数据结构和算法。

## 目录

  1) [apps](./apps/)
  2) [leetcode](./leetcode/)（题解+文档）
  3) [python/sgd_alg](./python/sgd_alg/)（算法库）
   
## 说明
  1、数据结构和算法实现汇总在python/sgd_alg库中。
  按下述方式可方便调用sgd_alg库中各种实现。
  ``` python
  %cd /playground/sgd_算法/
  import sys  
  sys.path.append('./python')
  ```
2、apps：使用notebook对算法库中的各部分做文档说明，并以例子的形式说明各算法api的调用方式（暂时充当api文档和测试的功能）。

3、leetcode：总结了一些重要的刷题经验，包括文档和具体代码

## 已实现
  - context【常用场景下的算法】
    - 水塘抽样算法
    - 字典树(trie tree)
    - bloom filter
    - cache 调度算法
      - LRU缓存
  - data_struct【数据结构】
    - Stack
      - 单调栈
      - 普通栈
    - 集合 Bag
    - 堆 Heap
    - 队列 Queue
    - 并查集 Union-Find
  
  - search 搜索算法
    - 哈希表
      - 静态hash表
    - 二分查找
    - 二分查找树
    - symbol_table
  
  - shuffle
    - knuth-shuffle
    - shuffle_sort

  - sort 排序算法
    - 归并排序 Merge Sort
    - 快排 Quick Sort
    - 堆排序
    - 插入排序
    - 选择排序
    - 希尔排序
  

