def binary_search(nums, key):
    """ 二分查找，
    :param nums: 有序数组
    :param key: 查找值
    :return: 成功返回index，失败返回-1
    """
    p_s, p_e = 0, len(nums) - 1

    while p_s <= p_e:
        p_mid = (p_s + p_e) // 2
        if nums[p_mid] == key:
            return p_mid
        elif key < nums[p_mid]:
            p_e = p_mid - 1
        else:
            p_s = p_mid + 1

    return -1


# 二分查找变体，剑指offer
