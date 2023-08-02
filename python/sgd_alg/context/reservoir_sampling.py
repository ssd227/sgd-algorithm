"""
水塘抽样算法
    当内存无法加载全部数据时，
    如何从包含未知大小的数据流中随机选取k个数据，
    并且要保证每个数据被抽取到的概率相等。

tips:
    keep_num = k 只考虑蓄水池为k的算法（可以推广到k=1）
    并且事先不需要知道抽样数据流的大小，最终每个数据被抽样的概率为 1/N。


参考：https://zhuanlan.zhihu.com/p/29178293
"""
import random


def reservoir_sampling(data_stream, keep_num=1):
    res = []
    i = 0
    for item in data_stream:
        i += 1  # 计数
        # 以概率1保留前N各数
        if len(res) < keep_num:
            res.append(item)
        else:
            # 对于第i个数，以概率k/i保留， 并随机占据任意位置
            p_i = 1.0 * keep_num / i
            if random.random() <= p_i:  # [0, 1]随机分布
                # 随机替换前k个数中的一个
                rand_id = random.randint(0, keep_num - 1)
                res[rand_id] = item
    return res



