# sgd_algorithm（python-version）

## 简介
以《algorithm 4th》为基本框架，整合常用的数据结构和算法。

文件结构如下：
* [apps](./apps/) （examples）
* [leetcode](./leetcode/)（题解+docs）
* [python/sgd_alg](./python/sgd_alg/)（src code）
   
## Note
* 数据结构和算法实现汇总在python/sgd_alg库中。
  按下述方式可方便调用sgd_alg库中各种实现。
  ``` python
  %cd 主目录 # notebook中使用cd ../../
  import sys  
  sys.path.append('./python')
  ```
* apps：使用notebook对算法库中的各部分做文档说明，并以例子的形式说明各算法api的调用方式（暂时充当api文档和测试的功能）

* leetcode：总结了一些重要的刷题经验，包括文档和具体代码

---
## Content

  - data_struct 数据结构
    - Stack
      - [X] 普通栈 [[code]](./python/sgd_alg/data_struct/stack/stack.py) [[app]](./apps/data_struct/stack.ipynb)
      - [X] 单调栈 [[code]](./python/sgd_alg/data_struct/stack/monstack.py) [[app]](./apps/data_struct/stack.ipynb)
    - [X] 集合 Bag [[code]](./python/sgd_alg/data_struct/bag.py) [[app]](./apps/data_struct/bag.ipynb)
    - [X] 堆 Priority Heap [[code]](./python/sgd_alg/data_struct/heap.py) [[app]](./apps/data_struct/priority_heap.ipynb)
    - [X] 队列 Queue [[code]](./python/sgd_alg/data_struct/queue.py) [[app]](./apps/data_struct/queue.ipynb)
    - [X] 并查集 Union-Find [[code]](./python/sgd_alg/data_struct/union_find.py) [[app]](./apps/data_struct/union_find.ipynb) 
  
  - search 搜索算法
    - symbol_table
      - [X] 二分查找 [[code]](./python/sgd_alg/search/binary_search.py) [[app]](./apps/search/binary_search.ipynb)
      - [X] binary search Tree (BST) 二分查找树 [[code]](./python/sgd_alg/search/binary_search_tree.py) [todo]
      - [X] left lean red black tree (LLRBT) 红黑树 [[code]](./python/sgd_alg/search/read_black_tree.py) [todo]
      - [X] skip list 跳跃表 [[code]](./python/sgd_alg/search/binary_search_tree.py) [todo]
  
    - Hash Table
      - [X] 静态hash表 [[code]](./python/sgd_alg/search/hash_table/static_hashing/) [[app]](./apps/search/hash_table.ipynb)

  
  - shuffle
    - [X] knuth-shuffle [[code]](./python/sgd_alg/shuffle/knuth_shuffle.py) [[app]](./apps/shuffle/knuth_shuffle.ipynb) 
    - [X] shuffle_sort [[code]](./python/sgd_alg/shuffle/shuffle_sort.py) [[app]](./apps/shuffle/shuffle_sort.ipynb) 

  - sort 排序算法
    - [X] Merge Sort 归并排序 [[code]](./python/sgd_alg/sort/merge_sort/) [[app]](./apps/sort/merge_sort.ipynb) 
    - [X] Quick Sort 快排 [[code]](./python/sgd_alg/sort/quick_sort/) [[app]](./apps/sort/quick_sort.ipynb) 
    - [X] 堆排序  [[code]](./python/sgd_alg/sort/heap_sort.py) [[app]](./apps/sort/basic_sort.ipynb) 
    - [X] 插入排序  [[code]](./python/sgd_alg/sort/insertion_sort.py) [[app]](./apps/sort/basic_sort.ipynb) 
    - [X] 选择排序 [[code]](./python/sgd_alg/sort/selection_sort.py) [[app]](./apps/sort/basic_sort.ipynb) 
    - [X] 希尔排序 [[code]](./python/sgd_alg/sort/shell_sort.py) [[app]](./apps/sort/basic_sort.ipynb) 

  - string 字符串
    - [X] trie tree 字典树 [[code]](./python/sgd_alg/context/trie_tree.py) [[app]](./apps/context/trie_tree.ipynb) 
    - substring search 子串匹配
        - [X] Knuth-Morris-Pratt [[code]](./python/sgd_alg/strings/substring_search/kmp.py) [[app]](./apps/strings/substring_search.ipynb)
        - [X] Boyer-Moore [[code]](./python/sgd_alg/strings/substring_search/bm.py) [[app]](./apps/strings/substring_search.ipynb)
        - [X] Rabin-Karp [[code]](./python/sgd_alg/strings/substring_search/rk.py) [[app]](./apps/strings/substring_search.ipynb)

  - regular expression 正则表达式

  - context 常用场景下的算法
    - [X] 水塘抽样算法 [[code]](./python/sgd_alg/context/reservoir_sampling.py) [[app]](./apps/context/reservoir_sampling.ipynb) 
  
    - [X] bloom filter [[code]](./python/sgd_alg/context/bloom_filter/bloom_filter.py) [[app]](./apps/context/bloomFilter.ipynb) 
    - cache 调度算法
      - [X] LRU缓存 [[code]](./python/sgd_alg/context/cache/lru_cache.py) [[app]](./apps/context/cache.ipynb)