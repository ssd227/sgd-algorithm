相关题目

[347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)

[703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)


```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

方法1：朴素解法
```
时间复杂度：O(NlogN)
空间复杂度：O(N)

    1、遍历一遍数组，使用字典统计每个元素的出现次数。 O(N)
    2、使用排序算法对所有统计对 key-count 按照count排序。O(NlogN)
    3、返回排序后的前topk个key
```

方法2：局部淘汰法（“冒泡排序”获取TopK）
```
时间复杂度：
空间复杂度：

```

方法3：局部淘汰法（数据结构"堆"获取TopK）
```
时间复杂度：
空间复杂度：

```

方法4：
```
时间复杂度：
空间复杂度：

```




参考：
https://cloud.tencent.com/developer/article/1383458
