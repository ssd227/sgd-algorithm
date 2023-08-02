def binary_search(nums, target):
    """ 
        二分查找
        :param nums: 有序数组
        :param target: 查找值
        
        :return: 
            查找成功, 返回index
            查找失败, 返回-1
    """
    p_s, p_e = 0, len(nums) - 1
    while p_s <= p_e:
        p_mid = (p_s + p_e) // 2
        if nums[p_mid] == target:
            return p_mid
        elif target < nums[p_mid]:
            p_e = p_mid - 1
        else:
            p_s = p_mid + 1
    return -1
