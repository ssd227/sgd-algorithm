# 定义二分查找
def binary_search(nums, head, tail, key):
    """ 二分查找，
    :param nums: 有序数组
    :param key: 查找值
    :return: 成功返回index，失败返回-1
    """
    p_s, p_e = head, tail

    while p_s <= p_e:
        p_mid = (p_s + p_e) // 2
        if nums[p_mid] == key:
            return p_mid
        elif key < nums[p_mid]:
            p_e = p_mid - 1
        else:
            p_s = p_mid + 1
    return -1


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)  # NlgN 快排去重
        res = dict()
        ph = 0  # pointer of head
        while ph < len(nums) and nums[ph] <= 0:
            pe = len(nums) - 1  # pointer of end
            while nums[pe] >= 0:
                if ph + 1 >= pe:  # 头尾指针相邻跳出循环
                    break
                a, c = nums[ph], nums[pe]
                b = -(a + c)
                # 二分查找key，复杂的lgN
                if binary_search(nums, ph+1, pe-1) != -1:
                    res[(a, b, c)] = 1
                pe -= 1
            ph += 1
        return list(res.keys())
